# Generated by Django 3.1.2 on 2020-11-25 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0020_auto_20201125_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='time_register',
            field=models.CharField(blank=True, default=datetime.datetime(2020, 11, 25, 20, 30, 27, 118545), max_length=100),
        ),
    ]
