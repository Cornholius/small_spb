import time
from django.db import models
from django.urls import reverse


class MeterReadings(models.Model):

    area_number = models.CharField(max_length=60)
    personal_account = models.CharField(max_length=60)
    current_day = models.IntegerField(default=0)
    current_night = models.IntegerField(default=0)

    def __str__(self):
        return self.area_number

    class Meta:
        verbose_name = 'Показания электро энергии'
        verbose_name_plural = 'Показания электро энергии'


class News(models.Model):
    title = models.CharField(max_length=60)
    text = models.CharField(max_length=3000)

    def get_absolute_url(self):
        return reverse('news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-id']


class Documents(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name


class Debtors(models.Model):
    debtor = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.debtor
