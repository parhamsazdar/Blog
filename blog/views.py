from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from khayyam import JalaliDatetime
from .user_func import *
from blog.forms import Comment
from blog.models import Post, User_info, Category

from datetime import timedelta



def index(request):
    categories = Category.objects.all()
    latest_post = Post.objects.filter(active=True, confirm=True).order_by('-date_pub')[:3]
    popular_post = Post.objects.annotate(like_count=Count('like')).order_by('-like_count')[:3]

    return render(request, "blog/index.html",
                  {"categories": categories, "latest_post": latest_post, "popular_post": popular_post,
                   "most_prolific_user": prolific_user(Post,User),"popular_user":popular_user(User)})


def test(request):
    categories = Category.objects.all()
    latest_post = Post.objects.filter(active=True, confirm=True).order_by('-date_pub')[:4]
    popular_post = Post.objects.annotate(like_count=Count('like')).order_by('-like_count')[:4]
    return render(request, "blog/test.html",
                  {"categories": categories, "latest_post": latest_post, "popular_post": popular_post})


def test_2(request):
    categories = Category.objects.all()
    return render(request, "blog/test_2.html", {"categories": categories})


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    if post.confirm and post.active:
        form = Comment()
        return render(request, "blog/post.html",
                      context={"post": post, "form": form, "categories": categories})
    else:
        return HttpResponseForbidden("این پست از دسترس خارج است")
