# Generated by Django 3.1.1 on 2021-02-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
    ]