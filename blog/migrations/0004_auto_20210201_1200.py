# Generated by Django 3.1.1 on 2021-02-01 08:30

from django.conf import settings
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20210130_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_dislike_comments', related_query_name='user_dislike_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_like_comments', related_query_name='user_like_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_dislike_post', related_query_name='user_dislike_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='uploads/', verbose_name='عکس پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_like_post', related_query_name='user_like_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='متن'),
        ),
    ]
