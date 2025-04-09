from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from persiantools.jdatetime import JalaliDateTime


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    jalali_created_at = models.CharField(
        max_length=20, blank=True, null=True, validators=[RegexValidator(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}')]
        )
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.jalali_created_at:
            self.jalali_created_at = JalaliDateTime(self.created_at).strftime(
                "%Y/%m/%d %H:%M:%S"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, verbose_name=_('پست'))
    text = models.TextField(_("متن"))
    
    def __str__(self):
        return f'{self.post.title} - {self.pk} نظر'