# Generated by Django 3.1.1 on 2021-02-15 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210215_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='title',
        ),
    ]
