from django.db import models
from django.contrib.auth.models import User
import datetime
from phonenumber_field.modelfields import PhoneNumberField




TRAINING_PURPOSE = (
    ('', 'Mục tiêu tập luyện'),
    ('tc', 'Tăng cơ'),
    ('gm', 'Giảm mỡ'),
    ('sk', 'Duy trì sức khỏe'),
)




class register(models.Model):
    name = models.CharField(max_length=35)
    phone = models.CharField(max_length=11)
    purpose = models.CharField(choices=TRAINING_PURPOSE, max_length=100)
    time_register = models.CharField(default=datetime.datetime.now(), blank=True, max_length=100)
    def __str__(self):
        return self.name


