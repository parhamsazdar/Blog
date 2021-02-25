from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import PostSearchForm
from .stop_word import stemmer
from .user_func import *
from blog.models import Post, Category, Tags, Word


def index(request):
    """
    Providing latest post & popular post & prolific user &  popular user
    for index template.
    """
    latest_post = Post.objects.filter(active=True, confirm=True).order_by('-date_pub')[:3]
    popular_post = Post.objects.filter(confirm=True, active=True).annotate(like_count=Count('like')).order_by(
        '-like_count')[:3]

    return render(request, "blog/index.html",
                  {"latest_post": latest_post, "popular_post": popular_post,
                   "most_prolific_user": prolific_user(Post, User), "popular_user": popular_user(User)})


class WirterPost(generic.DetailView):
    """
    Return all the post of specific writer.
    """
    model = User

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        header = f"جدیدترین پست های {user.first_name + ' ' + user.last_name}"
        context = {'posts': user.post.filter(confirm=True, active=True), "header": header}
        return render(request, 'blog/writer_post.html', context)


class TagsPost(generic.DetailView):
    """
       Return all the post of specific tag.
    """
    model = Tags

    def get(self, request, *args, **kwargs):
        tag = get_object_or_404(Tags, pk=kwargs['pk'])
        header = f"جدیدترین پست های بر چسب {tag.name}"
        context = {'posts': tag.post_set.filter(confirm=True, active=True), "header": header}
        return render(request, 'blog/tag_post.html', context)


class SubCategoryPost(generic.DetailView):
    """
       Return all the post of specific category.
    """
    model = Category

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs['pk'])
        header = f"جدیدترین پست های {category.name}"
        context = {'post_of_cat': category.post.filter(confirm=True, active=True).order_by('-date_pub'),
                   "header": header, "category": [category]}
        return render(request, 'blog/subcategory.html', context)


class PostShow(generic.DetailView):
    """
    Return a specific post.
    """
    model = Post
    template_name = 'blog/post.html'
    context_object_name = "post"

    def get_queryset(self):
        qs = super(PostShow, self).get_queryset()
        return qs.filter(confirm=True, active=True)


class LatestPost(generic.ListView):
    """
    Return all post order by pub date
    """
    template_name = 'blog/latest_post.html'
    context_object_name = "latest_post"

    def get_context_data(self, **kwargs):
        context = super(LatestPost, self).get_context_data(**kwargs)
        context['header'] = "جدیدترین پست ها"
        return context

    def get_queryset(self):
        return Post.objects.filter(active=True, confirm=True).order_by('-date_pub')


class PopularPost(generic.ListView):
    """
    Return all post order by count of like
    """
    template_name = 'blog/popular_post.html'
    context_object_name = "popular_post"

    def get_context_data(self, **kwargs):
        context = super(PopularPost, self).get_context_data(**kwargs)
        context['header'] = "محبوب ترین پست ها"
        return context

    def get_queryset(self):
        return Post.objects.filter(confirm=True, active=True).annotate(like_count=Count('like')).order_by('-like_count')


def log_out(request):
    """
    logout the user
    """
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def search_post(request):
    """
    This view receive query pram with method get that I named it search word.
    I use search word for searching in my database. But the point is search word can
    appear in title or text or tags or ... of the post.
    This view is action simple search form 9in my menubar.
    """
    word = request.GET.get('search_word')
    if word:
        queryset = Post.objects.filter(confirm=True, active=True).filter(
            Q(title__contains=word) | Q(user__first_name__contains=word) |
            Q(user__last_name__contains=word) | Q(tags__name__contains=word)).distinct(
            'title')
        word_in_text = Word.objects.filter(word=stemmer(word))
        if len(word_in_text) > 0:
            posts = word_in_text[0].post.all()
            queryset = queryset.union(queryset, posts)
        header = f"نتیجه جستجوی عبارت {word}"
        return render(request, 'blog/search_result.html', {"posts": queryset, "header": header})
    else:
        return render(request, 'blog/search_result.html', {"header": "عبارت مورد نظر یافت نشد"})


def search_porefessional(request):
    """
    This view receive query pram with method get that I named it search word.
    I use search word for searching in my database. But it use for porefessional search and
    operator "and" established between my lookup query
    """
    if request.POST:
        form = PostSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posts = Post.objects.filter(confirm=True, active=True,
                                        title__contains=data['title'],
                                        user__first_name__contains=data["first_name"],
                                        user__last_name__contains=data["last_name"],
                                        tags__name__contains=data["tag"],
                                        word__word__contains=stemmer(data["word"])).distinct('title')

            if posts:
                header = "نتیجه جستجو"
            else:
                header = "نتیجه ای یافت نشد"
            return render(request, 'blog/search_result.html', {"posts": posts, "header": header})
