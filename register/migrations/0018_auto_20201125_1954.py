# Generated by Django 3.1.2 on 2020-11-25 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_auto_20201123_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='purpose',
            field=models.CharField(choices=[('tc', 'Tăng cơ'), ('gm', 'Giảm mỡ'), ('sk', 'Duy trì sức khỏe')], default='Mục tiêu tập luyện', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='time_register',
            field=models.CharField(blank=True, default=datetime.datetime(2020, 11, 25, 19, 54, 25, 115343), max_length=100),
        ),
    ]
