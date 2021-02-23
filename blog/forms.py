from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, ChoiceField
from django import forms
from blog.models import Comments, Post, Word


class PostSearchForm(ModelForm):
    class Meta:
        labels = {
            "title":"عنوان پست",
            "tags":"برچسب",
        }
        model = Post
        fields = ['title', 'tags']
        widgets = {"tags": forms.TextInput()}
    wirter_first_name=forms.CharField(label='نام نویسنده')
    wirter_last_name=forms.CharField(label= 'نام خانوادگی نویسنده')
    word =forms.CharField(max_length=50,label='کلمه کلیدی در پست')

# class UserSearchForm(ModelForm):
#     class Meta:
#         labels = {
#             "first_name": "نام نویسنده",
#             "last_name": "نام خانوادگی نویسنده"
#         }
#         model = User
#         fields = ['first_name', 'last_name']
