from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from persiantools.jdatetime import JalaliDateTime

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    jalali_created_at = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[RegexValidator(r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}")],
    )
    likes = models.ManyToManyField(
        User, related_name="liked_posts", blank=True, verbose_name="لایک ها"
    )
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    video = models.FileField(upload_to="post_videos/", null=True, blank=True)
    audio = models.FileField(upload_to="post_audio/", null=True, blank=True)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.jalali_created_at:
            self.jalali_created_at = JalaliDateTime(self.created_at).strftime(
                "%Y/%m/%d %H:%M:%S"
            )
        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, default=1, related_name='comments')
    post = models.ForeignKey(Post, models.CASCADE, verbose_name=_("پست"))
    text = models.TextField(_("متن"))

    def __str__(self):
        return f"{self.post.title} - {self.pk} نظر"
