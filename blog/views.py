from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .user_func import *
from blog.forms import Comment
from blog.models import Post, Category, Tags
from django.contrib import messages

def index(request):
    latest_post = Post.objects.filter(active=True, confirm=True).order_by('-date_pub')[:3]
    popular_post = Post.objects.annotate(like_count=Count('like')).order_by('-like_count')[:3]

    return render(request, "blog/index.html",
                  {"latest_post": latest_post, "popular_post": popular_post,
                   "most_prolific_user": prolific_user(Post, User), "popular_user": popular_user(User)})


def writer_post(request, writer_id):
    post = Post.objects.filter(user__pk=writer_id).order_by("-date_pub")
    writer = User.objects.filter(pk=writer_id)
    return render(request, 'blog/writer_post.html', {"posts": post, "writer": writer})


def post_tag(request, tag_id):
    tag = Tags.objects.filter(pk=tag_id)
    post = Post.objects.filter(tags__in=tag).order_by('-date_pub')
    return render(request, 'blog/tag_post.html', {"posts": post, "tag": tag})


def suc_category(request, cat_id):
    post_of_cat = Post.objects.filter(category__id=cat_id).order_by('-date_pub')
    category = Category.objects.filter(pk=cat_id)

    return render(request, "blog/subcategory.html", {"post_of_cat": post_of_cat, "category": category})


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.confirm and post.active:
        form = Comment()
        return render(request, "blog/post.html",
                      context={"post": post, "form": form})
    else:
        return HttpResponseForbidden("این پست از دسترس خارج است")


def log_out(request):
    logout(request)
    # messages.success(request, 'خروج با موفقیت انجام شد')
    return redirect('blog:index')