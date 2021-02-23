from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, ChoiceField
from django import forms

from blog.models import Comments, Post, Word


class PostSearchForm(forms.Form):
    title = forms.CharField(label='عنوان پست', max_length=50, required=False)
    tag = forms.CharField(max_length=30, label='برچسب', required=False)
    first_name = forms.CharField(label='نام نویسنده', required=False)
    last_name = forms.CharField(label='نام خانوادگی نویسنده', required=False)
    word = forms.CharField(max_length=50, label='کلمه کلیدی در پست', required=False)

