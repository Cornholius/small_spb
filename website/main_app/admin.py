from django.contrib import admin
from .models import MeterReadings, News, Documents, Debtors


admin.site.site_title = 'ololo1'
admin.site.site_header = 'ololo2'


class MeterReadingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'area_number', 'personal_account', 'current_day', 'current_night')
    search_fields = ('area_number', 'personal_account')
    list_editable = ('area_number', 'personal_account', 'current_day', 'current_night')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    search_fields = ('title', 'text')


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')
    search_fields = ['name']


class DebtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_order', 'personal_account', 'last_paid_month')
    list_editable = ('payment_order', 'personal_account', 'last_paid_month')
    search_fields = ('payment_order', 'personal_account', 'last_paid_month')


admin.site.register(MeterReadings, MeterReadingsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Debtors, DebtorsAdmin)