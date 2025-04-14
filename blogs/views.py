from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import CommentForm
from .models import Post, Comment


def home(request):
    return render(request, "blogs/home.html")


def about_view(request):
    return render(request, "blogs/about.html")


def post_view(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blogs/post.html", {"posts": posts})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Login required"}, status=401)

        existing_comments = post.comments.filter(user=request.user)
        if existing_comments.count() >= 5:
            return JsonResponse(
                {"error": "شما بیش از ۵ نظر برای این پست ثبت کرده‌اید!"}, status=403
            )

        form = CommentForm(request.POST)
        if form.is_valid():
            # breakpoint()
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return JsonResponse(
                {
                    "user": comment.user.username,
                    "text": comment.text,
                    "jalali_created_at": comment.jalali_created_at,
                }
            )
        else:
            return JsonResponse({"error": "فرم نامعتبر است"}, status=400)

    return render(
        request,
        "blogs/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        },
    )


@require_POST
@login_required
def like_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({"liked": liked, "total_likes": post.likes.count()})
