from django.forms import ModelForm

from blog.models import Comments


class Comment(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
