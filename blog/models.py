from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


class Text(models.Model):
    text = HTMLField(verbose_name='متن')
    confirm = models.BooleanField('تایید', default=False)
    date_pub = models.DateTimeField(verbose_name="تاریخ انتشار", auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='%(class)s',
                             verbose_name='کاربر')
    like = models.ManyToManyField(User, related_name="%(class)s_likedby", related_query_name="%(class)s_likedby",
                                  blank=True, null=True)
    dislike = models.ManyToManyField(User, related_name="%(class)s_dislikedby",
                                     related_query_name="%(class)s_dislikedby", blank=True, null=True)



    class Meta:
        abstract = True




class Post(Text):
    class Meta(Text.Meta):
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        permissions = [
            ("confirm_post", "تایید کردن"),
            ("active_post", "فعال کردن")
        ]
    title = models.CharField('عنوان', max_length=50)
    active = models.BooleanField('فعال', default=True)
    image = models.ImageField(verbose_name='عکس پست', upload_to='uploads/post_image', null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name="دسته بندی",on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tags', verbose_name="برجسب ها")

    def __str__(self):
        return self.title

class Comments(Text):
    class Meta(Text.Meta):
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        permissions = [
            ("confirm_comment", "تایید کردن"),
            ("active_comment", "فعال کردن")
        ]

    post = models.ForeignKey(Post, related_name="comment", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    name = models.CharField('عنوان دسته بندی', max_length=30)
    icon = models.CharField('fontawesome', max_length=100, null=True)
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


class UserInfo(models.Model):
    phone = models.IntegerField('شماره تلفن', null=True, blank=True)
    photo = models.ImageField(verbose_name='عکس کاربر', upload_to='uploads/user_photo')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='آیدی کاربری', related_name='info',
                                null=True)

    def __str__(self):
        return str(self.user)


class MainContent(models.Model):
    class Meta:
        verbose_name = 'محتوای اصلی'
        verbose_name_plural = "محتوای اصلی"

    image = models.ImageField(verbose_name='عکس اسلاید', upload_to='uploads/slide_show')
    title = models.CharField('عنوان', max_length=200)
    short_description = models.CharField('توضیح کوتاه', max_length=300)
