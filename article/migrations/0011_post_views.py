# Generated by Django 3.1.2 on 2020-11-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_remove_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]