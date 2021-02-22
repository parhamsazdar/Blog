from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

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


class WirterPost(generic.DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        header = f"جدیدترین پست های {user.first_name + ' ' + user.last_name}"
        context = {'posts': user.post.all(), "header": header}
        return render(request, 'blog/writer_post.html', context)


class TagsPost(generic.DetailView):
    model = Tags

    def get(self, request, *args, **kwargs):
        tag = get_object_or_404(Tags, pk=kwargs['pk'])
        header = f"جدیدترین پست های بر چسب {tag.name}"
        context = {'posts': tag.post_set.all(), "header": header}
        return render(request, 'blog/tag_post.html', context)


class SubCategoryPost(generic.DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs['pk'])
        header = f"جدیدترین پست های {category.name}"
        context = {'post_of_cat': category.post.order_by('-date_pub'), "header": header, "category": [category]}
        return render(request, 'blog/subcategory.html', context)


class PostShow(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = "post"

    def get_queryset(self):
        qs = super(PostShow, self).get_queryset()
        return qs.filter(confirm=True, active=True)


class LatestPost(generic.ListView):
    template_name = 'blog/latest_post.html'
    context_object_name = "latest_post"

    def get_context_data(self, **kwargs):
        context = super(LatestPost, self).get_context_data(**kwargs)
        context['header'] = "جدیدترین پست ها"
        return context

    def get_queryset(self):
        return Post.objects.filter(active=True, confirm=True).order_by('-date_pub')


class PopularPost(generic.ListView):
    template_name = 'blog/popular_post.html'
    context_object_name = "popular_post"

    def get_context_data(self, **kwargs):
        context = super(PopularPost, self).get_context_data(**kwargs)
        context['header'] = "محبوب ترین پست ها"
        return context

    def get_queryset(self):
        return Post.objects.annotate(like_count=Count('like')).order_by('-like_count')


def log_out(request):
    logout(request)
    # messages.success(request, 'خروج با موفقیت انجام شد')
    return redirect(request.META.get('HTTP_REFERER'))



def test_search(request):
    if request.POST:
        if request.POST["keyword"]:
            post=Post.objects.filter(title__contains=request.POST['keyword'])
            if len(post)>0:
                return JsonResponse({'data':post[0].title,'src':post[0].image.url})
        return JsonResponse({"data":"cant find"})