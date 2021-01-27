from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('عنوان', max_length=50)
    text = models.TextField('متن')
    image = models.ImageField(verbose_name='عکس پست')
    confirm = models.BooleanField('تایید')
    active = models.BooleanField('فعال')
    like = models.IntegerField()
    dislike = models.IntegerField()
    date_pub=models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('Category', through='Post_category', through_fields=('post', 'category'))
    tags = models.ManyToManyField('Tags', through='Post_tags', through_fields=('post', 'tags'))
    writer = models.ForeignKey('Writer', on_delete=models.PROTECT, related_name='posts', verbose_name='نویسنده')
    comments=models.ManyToManyField('Comments',through='Post_comments', through_fields=('post', 'comments'))

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('عنوان دسته بندی', max_length=30)
    parent = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='پدر',
                               related_name='subcategory')

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField('پرجسب', max_length=30)

    def __str__(self):
        return self.name


class Writer(models.Model):
    first_name = models.CharField("نام", max_length=10)
    last_name = models.CharField("نام خانوادگی", max_length=10)
    email = models.EmailField("ایمیل")
    photo = models.ImageField(verbose_name='عکس کاربر')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='آیدی کاربری', related_name='writer')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='writer_post')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Comments(models.Model):
    title=models.CharField('عنوان',max_length=20)
    text=models.TextField('متن')
    confirm = models.BooleanField('تایید')
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Post_category(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_cat', verbose_name='پست')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name='دسته بندی')

    def __str__(self):
        return self.post.title + '_' + self.category.name


class Post_tags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags', verbose_name='پست', null=True,
                             blank=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='tags', verbose_name='برچسب', null=True,
                             blank=True)

    def __str__(self):
        return self.post.title + '_' + self.tags.name


class Post_comments(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', verbose_name='پست', null=True,
                             blank=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comment', verbose_name='نظر', null=True,
                             blank=True)