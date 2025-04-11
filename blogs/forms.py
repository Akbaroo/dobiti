from django import forms
from .models import Comment


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
