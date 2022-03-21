from django.db import models


class MeterReadings(models.Model):

    area_number = models.CharField(max_length=60)
    personal_account = models.CharField(max_length=60)
    current_day = models.IntegerField(default=0)
    current_night = models.IntegerField(default=0)

    def __str__(self):
        return self.area_number


class News(models.Model):
    title = models.CharField(max_length=60)
    text = models.CharField(max_length=3000)

    def __str__(self):
        return self.title
