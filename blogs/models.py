from django.db import models
from django.core.validators import RegexValidator
from persiantools.jdatetime import JalaliDateTime


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    jalali_created_at = models.CharField(
        max_length=20, blank=True, null=True, validators=[RegexValidator(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}')]
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.jalali_created_at:
            self.jalali_created_at = JalaliDateTime(self.created_at).strftime(
                "%Y/%m/%d %H:%M:%S"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
