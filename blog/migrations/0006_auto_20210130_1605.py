# Generated by Django 3.1.1 on 2021-01-30 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210130_1558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('wirte_post', 'نوشتن مطلب در سایت'), ('edit_post', 'ویرایش مطلب در سایت'), ('comment_post', 'نظر گذاشتن برای مطلب در سایت')]},
        ),
    ]