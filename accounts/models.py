from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class UserManager(UserManager):
    pass


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64, blank=True, null=True) 

    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    def __str__(self):
        return self.username
