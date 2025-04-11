from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import CommentForm
from .models import Post, Comment


def home(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "home.html", {"posts": posts})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if len(Comment.objects.filter(user=request.user)) > 5:
            pass # TODO return a error massege
        elif comment.is_valid():
            Comment.objects.create(
                text = comment.cleaned_data["text"],
                user = request.user,
                post = post,
            )
    comment = CommentForm()
    context = {
        "post": post,
        'comment': comment,
        'comments': Comment.objects.all(),
    }
    return render(request, "blogs/post_detail.html", context=context)



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

    return JsonResponse({
        'liked': liked,
        'total_likes': post.likes.count()
    })
