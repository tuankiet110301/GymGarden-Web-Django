# Generated by Django 3.1.2 on 2020-11-25 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_auto_20201125_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='time_register',
            field=models.CharField(blank=True, default=datetime.datetime(2020, 11, 25, 20, 2, 39, 89425), max_length=100),
        ),
    ]