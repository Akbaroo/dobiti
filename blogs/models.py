from django.urls import reverse
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from persiantools.jdatetime import JalaliDateTime

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    likes = models.ManyToManyField(
        User, related_name="liked_posts", blank=True, verbose_name="لایک ها", editable=False
    )
    image = models.ImageField(upload_to="post_images/")
    video = models.FileField(upload_to="post_videos/")
    audio = models.FileField(upload_to="post_audio/")

    # for google
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    # for users
    jalali_updated_at = models.CharField(  
        editable=False, max_length=20, blank=True,null=True,
        verbose_name="تاریخ ویرایش",
        validators=[RegexValidator(r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}")],
    )
    jalali_created_at = models.CharField(
        editable=False, max_length=20, blank=True,null=True,
        verbose_name="تاریخ ایجاد",
        validators=[RegexValidator(r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}")],
    )

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"

    def save(self, *args, **kwargs):
        if not self.jalali_created_at:
            super().save(*args, **kwargs)
            self.jalali_created_at = JalaliDateTime(self.created_at).strftime("%Y/%m/%d %H:%M:%S")
        
        self.jalali_updated_at = JalaliDateTime(self.updated_at).strftime("%Y/%m/%d %H:%M:%S")
        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User, models.CASCADE, blank=True, default=1, # admin
        related_name="comments", verbose_name=_("کاربر"),
    )
    post = models.ForeignKey(
        Post, models.CASCADE, verbose_name=_("پست"), related_name="comments"
    )
    text = models.TextField(_("متن"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    jalali_created_at = models.CharField(
        editable=False, max_length=20, blank=True, null=True,
        verbose_name="تاریخ ایجاد",
        validators=[RegexValidator(r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}")],
    )
    
    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def save(self, *args, **kwargs):
        if not self.jalali_created_at:
            super().save(*args, **kwargs)
            self.jalali_created_at = JalaliDateTime(self.created_at).strftime("%Y/%m/%d %H:%M:%S")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} on {self.post}"
