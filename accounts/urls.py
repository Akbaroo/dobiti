from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path("verify-email/<str:token>/", views.email_varify, name="email_varify"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]