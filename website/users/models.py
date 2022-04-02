from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from main_app.models import MeterReadings


class CustomUser(AbstractUser):

    area_numbers_list = []
    area_numbers = MeterReadings.objects.all()
    for i in area_numbers:
        area_numbers_list.append((f'{i.area_number}', f'{i.area_number}'))

    username = models.CharField(max_length=60, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=60, verbose_name='Имя')
    last_name = models.CharField(max_length=60, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=60, verbose_name='Отчество')
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    area_number = models.CharField(choices=area_numbers_list, default='', max_length=15)
