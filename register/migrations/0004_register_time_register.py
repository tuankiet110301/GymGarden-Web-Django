# Generated by Django 3.1.2 on 2020-11-16 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20201116_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='time_register',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 11, 16, 21, 18, 30, 822987)),
            preserve_default=False,
        ),
    ]
