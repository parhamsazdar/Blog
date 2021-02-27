from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, ChoiceField
from django import forms

from blog.models import Comments, Post, Word, UserInfo


class SignUpForm(UserCreationForm):
    """
    This form inherited from UserCreationForm default django for validations,
    this form used for sign-up user in site
    """
    phone_number = forms.CharField(label='شماره تلفن', max_length=20, required=False)
    image = forms.ImageField(label="عکس پروفایل", required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'image', 'phone_number',
                  'email', 'password1', 'password2',)


class PostSearchForm(forms.Form):
    """
    This is a form of professional search.
    """
    title = forms.CharField(label='عنوان پست', max_length=50, required=False)
    tag = forms.CharField(max_length=30, label='برچسب', required=False)
    first_name = forms.CharField(label='نام نویسنده', required=False)
    last_name = forms.CharField(label='نام خانوادگی نویسنده', required=False)
    word = forms.CharField(max_length=50, label='کلمه کلیدی در پست', required=False)

