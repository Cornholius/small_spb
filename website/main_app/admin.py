from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields


admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Панель управления'


class MeterReadingsResource(resources.ModelResource):

    area_number = fields.Field(column_name='№ участка', attribute='area_number')
    personal_account = fields.Field(column_name='№ лицевого счета', attribute='personal_account')
    current_day = fields.Field(column_name='показания день', attribute='current_day')
    current_night = fields.Field(column_name='показания ночь', attribute='current_night')

    class Meta:
        model = MeterReadings
        exclude = ['id']
        import_id_fields = ['area_number']


@admin.register(MeterReadings)
class MeterReadingsAdmin(ImportExportActionModelAdmin):
    resource_class = MeterReadingsResource
    list_display = ('area_number', 'personal_account', 'current_day', 'current_night')
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


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('photo', 'admin_image')
    readonly_fields = ('admin_image',)

admin.site.register(FAQ)
# admin.site.register(Gallery)
# admin.site.register(News, NewsAdmin)
# admin.site.register(Documents, DocumentsAdmin)
# admin.site.register(Debtors, DebtorsAdmin)
# admin.site.register(MainPicture)
