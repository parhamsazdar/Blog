from django.forms import ModelForm
from django import forms
from blog.models import Comments


class Comment(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]

