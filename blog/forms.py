from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import formset_factory, ModelForm
from django.forms import modelformset_factory

from blog.models import Comments


class Comment(ModelForm):
    class Meta:
        model=Comments
        fields=["text"]
