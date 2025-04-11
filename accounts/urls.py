from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'auth'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]