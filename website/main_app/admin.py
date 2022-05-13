from django.contrib import admin
from django.utils.html import format_html

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


class DebtorsResource(resources.ModelResource):
    payment_order = fields.Field(column_name='№ платёжного поручения', attribute='payment_order')
    personal_account = fields.Field(column_name='№ лицевого счёта', attribute='personal_account')
    debtor_fio = fields.Field(column_name='ФИО Собственника', attribute='debtor_fio')
    last_paid_month = fields.Field(column_name='Последний оплаченный месяц', attribute='last_paid_month')

    class Meta:
        model = Debtors
        import_id_fields = ['id']


@admin.register(MeterReadings)
class MeterReadingsAdmin(ImportExportActionModelAdmin):
    resource_class = MeterReadingsResource
    list_display = ('area_number', 'personal_account', 'current_day', 'current_night')
    search_fields = ('area_number', 'personal_account')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/news/{}/">Удалить</a>', obj.id)

    list_display = ('title', 'text', 'date', 'delete_button')
    search_fields = ('title', 'text')
    delete_button.short_description = ''


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    search_fields = ['name']

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/documents/{}/">Удалить</a>', obj.id)

    list_display = ('name', 'document', 'delete_button')
    delete_button.short_description = ''



@admin.register(Debtors)
class DebtorsAdmin(ImportExportActionModelAdmin):
    resource_class = DebtorsResource

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/debtors/{}/">Удалить</a>', obj.id)

    list_display = ('payment_order', 'personal_account', 'debtor_fio', 'last_paid_month', 'delete_button')
    search_fields = ('payment_order', 'personal_account', 'last_paid_month')
    delete_button.short_description = ''


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


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    search_fields = ['name']

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/faq/{}/">Удалить</a>', obj.id)

    list_display = ('question', 'answer', 'delete_button')
    delete_button.short_description = ''


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message_title', 'message_text', 'email')
