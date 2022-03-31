from django.contrib import admin
from .models import MeterReadings, News, Documents, Debtors, MainPicture
from import_export.admin import ImportExportActionModelAdmin


admin.site.site_title = 'ololo1'
admin.site.site_header = 'ololo2'


@admin.register(MeterReadings)
class MeterReadingsAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'area_number', 'personal_account', 'current_day', 'current_night')
    search_fields = ('area_number', 'personal_account')
    list_editable = ('current_day', 'current_night')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    search_fields = ('title', 'text')


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')
    search_fields = ['name']


@admin.register(Debtors)
class DebtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_order', 'personal_account', 'last_paid_month')
    list_editable = ('payment_order', 'personal_account', 'last_paid_month')
    search_fields = ('payment_order', 'personal_account', 'last_paid_month')


@admin.register(MainPicture)
class MainPictureAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(MeterReadings, MeterReadingsAdmin)
# admin.site.register(News, NewsAdmin)
# admin.site.register(Documents, DocumentsAdmin)
# admin.site.register(Debtors, DebtorsAdmin)
# admin.site.register(MainPicture)
