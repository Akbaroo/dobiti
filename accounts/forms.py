from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control mb-3", 'placeholder': 'نام کاربری'})
        self.fields['email'].widget.attrs.update({'class': "form-control mb-3", 'placeholder': 'ایمیل'})
        self.fields['email'].required = True
        self.fields['password1'].widget.attrs.update({'class': "form-control mb-3", 'placeholder': 'گذرواژه'})
        self.fields['password2'].widget.attrs.update({'class': "form-control mb-3", 'placeholder': 'تأیید گذرواژه'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control mb-3", 'placeholder': 'نام کاربری'})
        self.fields['password'].widget.attrs.update({'class': "form-control mb-3", 'placeholder': 'گذرواژه'})
