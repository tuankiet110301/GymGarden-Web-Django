# Generated by Django 3.1.2 on 2020-11-23 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]