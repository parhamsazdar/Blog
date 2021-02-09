from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils import timezone
from tinymce.models import HTMLField


class Text(models.Model):
    title = models.CharField('عنوان', max_length=50)
    text = HTMLField(verbose_name='متن')
    confirm = models.BooleanField('تایید', default=False)
    active = models.BooleanField('فعال', default=False)
    date_pub = models.DateTimeField(verbose_name="تاریخ انتشار",auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user_%(class)s',
                             verbose_name='کاربر')
    like = models.ManyToManyField(User, related_name="user_like_%(class)s", related_query_name="user_like_%(class)s",
                                  blank=True, null=True)
    dislike = models.ManyToManyField(User, related_name="user_dislike_%(class)s",
                                     related_query_name="user_dislike_%(class)s", blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     self.date_pub = timezone.now()
    #     super(Text, self).save(*args, **kwargs)

    class Meta:
        permissions = [
            ("confirm", "تایید کردن"),
            ("active", "فعال کردن")
        ]
        abstract = True

    def __str__(self):
        return self.title


class Post(Text):
    class Meta(Text.Meta):
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    image = models.ImageField(verbose_name='عکس پست', upload_to='uploads/post_image', null=True, blank=True)
    category = models.ManyToManyField('Category', verbose_name="دسته بندی")
    tags = models.ManyToManyField('Tags', verbose_name="برجسب ها")


class Comments(Text):
    class Meta(Text.Meta):
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    post = models.ForeignKey(Post, related_name="comment", null=True, blank=True, on_delete=models.CASCADE)


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    name = models.CharField('عنوان دسته بندی', max_length=30)
    icon=models.CharField('fontawesome',max_length=100,null=True)
    parent = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='پدر',
                               related_name='subcategory')

    def __str__(self):
        category = ''
        cat = self
        while cat.parent:
            category += cat.parent.name + " > "
            cat = cat.parent
        category += self.name
        return category


class Tags(models.Model):
    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"

    name = models.CharField('پرجسب', max_length=30)

    def __str__(self):
        return self.name


class User_info(models.Model):
    phone = models.IntegerField('شماره تلفن', null=True, blank=True)
    photo = models.ImageField(verbose_name='عکس کاربر', upload_to='uploads/user_photo')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='آیدی کاربری', related_name='user',
                                null=True)

    def __str__(self):
        return str(self.user)

# class Post_category(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_cat', verbose_name='پست')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name='دسته بندی')
#
#     def __str__(self):
#         return self.post.title + '_' + self.category.name


# class Post_tags(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags', verbose_name='پست', null=True,
#                              blank=True)
#     tags = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='tags', verbose_name='برچسب', null=True,
#                              blank=True)
#
#     def __str__(self):
#         return self.post.title + '_' + self.tags.name


# class Post_comments(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', verbose_name='پست',
#                              null=True,
#                              blank=True)
#     comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comment', verbose_name='نظر',
#                                  null=True,
#                                  blank=True)
