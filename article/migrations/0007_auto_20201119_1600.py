# Generated by Django 3.1.2 on 2020-11-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_post_thumbnail_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
