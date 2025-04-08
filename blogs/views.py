from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('-created_at')  # جدیدترین اول
    return render(request, 'home.html', {'posts': posts})
