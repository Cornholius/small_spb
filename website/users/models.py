from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# from website.main_app.models import MeterReadings


class CustomUser(AbstractUser):
    area_numbers = []

    first_name = models.CharField(max_length=60, verbose_name='Имя')
    last_name = models.CharField(max_length=60, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=60, verbose_name='Отчество')
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    area_number = models.CharField(choices=area_numbers, default='', max_length=1)