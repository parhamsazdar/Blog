from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from khayyam import JalaliDatetime

from blog.forms import Comment
from blog.models import Post, User_info, Category

from datetime import timedelta


def index(request):
    categories = Category.objects.all()
    latest_post = Post.objects.all().order_by('-date_pub')[:4]
    return render(request, "blog/index.html", {"latest_post": latest_post,"categories":categories})


def test(request):
    categories = Category.objects.all()
    latest_post = Post.objects.all().order_by('-date_pub')[:3]
    return render(request, "blog/test.html", {"categories": categories,"latest_post":latest_post})


def test_2(request):
    categories = Category.objects.all()
    return render(request, "blog/test_2.html", {"categories": categories})

def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    if post.confirm and post.active:
        form = Comment()
        return render(request, "blog/post.html",
                      context={"post": post, "form": form,"categories":categories})
    else:
        return HttpResponseForbidden("این پست از دسترس خارج است")
