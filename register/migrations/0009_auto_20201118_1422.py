# Generated by Django 3.1.2 on 2020-11-18 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20201118_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='time_register',
            field=models.CharField(blank=True, default=datetime.datetime(2020, 11, 18, 14, 22, 50, 180146), max_length=100),
        ),
    ]