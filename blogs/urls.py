from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about_view, name='about'),
    path('posts/', views.post_view, name='posts'),
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('posts/<int:post_id>/like/', views.like_post_view, name='like_post'),
]