from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


class Text(models.Model):
    title = models.CharField('عنوان', max_length=50)
    text = HTMLField(verbose_name='متن')
    confirm = models.BooleanField('تایید', default=False)
    active = models.BooleanField('فعال', default=False)
    date_pub = models.DateTimeField(verbose_name="تاریخ انتشار", auto_now_add=True)
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
        abstract = True

    def __str__(self):
        return self.title


class Post(Text):
    class Meta(Text.Meta):
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        permissions = [
            ("confirm_post", "تایید کردن"),
            ("active_post", "فعال کردن")
        ]

    image = models.ImageField(verbose_name='عکس پست', upload_to='uploads/post_image', null=True, blank=True)
    category = models.ManyToManyField('Category', verbose_name="دسته بندی")
    tags = models.ManyToManyField('Tags', verbose_name="برجسب ها")


class Comments(Text):
    class Meta(Text.Meta):
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        permissions = [
            ("confirm_comment", "تایید کردن"),
            ("active_comment", "فعال کردن")
        ]

    post = models.ForeignKey(Post, related_name="comment", null=True, blank=True, on_delete=models.CASCADE)


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


class User_info(models.Model):
    phone = models.IntegerField('شماره تلفن', null=True, blank=True)
    photo = models.ImageField(verbose_name='عکس کاربر', upload_to='uploads/user_photo')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='آیدی کاربری', related_name='user',
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
