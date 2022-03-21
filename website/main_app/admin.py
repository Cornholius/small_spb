from django.contrib import admin
from .models import MeterReadings, News

admin.site.register(MeterReadings)
admin.site.register(News)