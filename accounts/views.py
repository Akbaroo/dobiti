import string, random

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, get_user_model, login
from django.contrib import messages

from .forms import CustomUserCreationForm, LoginForm

User = get_user_model()

def generate_verification_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=64))

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            verification_token = generate_verification_token()
            user.verification_token = verification_token
            user.save()
            
            # send email
            current_site = get_current_site(request)
            subject = 'تایید ایمیل شما'
            message = render_to_string('accounts/verification_email.html', {
                'user': user,
                'domain': current_site.domain,
                'token': verification_token,
            })
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            
            next_url = request.GET.get('next', '/')
            return redirect(reverse("auth:email_varify") + f"?next={next_url}")

    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    next_url = request.GET.get('next', "/")
    return redirect(next_url)


def email_varify(request, token):
    try:
        user = User.objects.get(verification_token=token)
    except User.DoesNotExist:
        raise Http404("Invalid token")

    user.is_verified = True
    user.verification_token = ''  
    user.save()

    next_url = request.GET.get('next', '/')
    return redirect(reverse("auth:login") + f"?next={next_url}")

class LoginView(auth_views.LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_verified:
            # اگر کاربر تأیید نشده، به صفحه‌ی تأیید ایمیل هدایت میشه
            logout(user)
            messages.warning(self.request, "لطفاً ابتدا ایمیل خود را تأیید کنید.")
            next_url = self.request.GET.get('next', '/')
            return redirect(reverse("auth:email_varify") + f"?next={next_url}")
        # در غیر این صورت، لاگین انجام میشه
        login(self.request, user)
        return super().form_valid(form)