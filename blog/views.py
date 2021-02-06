from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.forms import Comment
from blog.models import Post, User_info


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.confirm and post.active:
        wirte = User_info.objects.get(user=post.user)
        if request.user.is_authenticated:
            user_photo = request.user.user.photo
        else:
            user_photo = None
        form = Comment()
        return render(request, "blog/post.html",
                      context={"post": post, "photo": wirte.photo, "user_photo": user_photo, "form": form})
    else:
        return HttpResponseForbidden("این پست از دسترس خارج است")



