from django.contrib import admin
from .models import MeterReadings, News, Documents, Debtors

admin.site.register(MeterReadings)
admin.site.register(News)
admin.site.register(Documents)
admin.site.register(Debtors)

admin.site.site_title = 'ololo1'
admin.site.site_header = 'ololo2'
