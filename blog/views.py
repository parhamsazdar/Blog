from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .user_func import *
from blog.forms import Comment
from blog.models import Post, Category





def index(request):

    latest_post = Post.objects.filter(active=True, confirm=True).order_by('-date_pub')[:3]
    popular_post = Post.objects.annotate(like_count=Count('like')).order_by('-like_count')[:3]

    return render(request, "blog/index.html",
                  { "latest_post": latest_post, "popular_post": popular_post,
                   "most_prolific_user": prolific_user(Post,User),"popular_user":popular_user(User)})


def suc_category(request,cat_id):
    post_of_cat=Post.objects.filter(id=cat_id).order_by('-date_pub')
    category=Category.objects.filter(pk=cat_id)

    return render(request,"blog/subcategory.html",{"post_of_cat":post_of_cat,"category":category})


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    if post.confirm and post.active:
        form = Comment()
        return render(request, "blog/post.html",
                      context={"post": post, "form": form, "categories": categories})
    else:
        return HttpResponseForbidden("این پست از دسترس خارج است")
