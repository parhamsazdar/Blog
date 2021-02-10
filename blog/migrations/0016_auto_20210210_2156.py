# Generated by Django 3.1.1 on 2021-02-10 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210210_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'permissions': [('confirm_comment', 'تایید کردن'), ('active_comment', 'فعال کردن')], 'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('confirm_post', 'تایید کردن'), ('active_post', 'فعال کردن')], 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
    ]
