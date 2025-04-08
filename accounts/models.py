from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class UserManager(UserManager):
    pass


class User(AbstractUser):

    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.username
