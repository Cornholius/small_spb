from .utils import rename_main_picture
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse


class MeterReadings(models.Model):

    area_number = models.CharField(max_length=60, verbose_name='№ участка')
    personal_account = models.CharField(max_length=60, verbose_name='№ лицевого счета')
    current_day = models.IntegerField(default=0, verbose_name='текущие показания день')
    current_night = models.IntegerField(default=0, verbose_name='текущие показания ночь')

    def __str__(self):
        return self.area_number

    class Meta:
        verbose_name = 'Показания электро энергии'
        verbose_name_plural = 'Показания электро энергии'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    text = models.CharField(max_length=3000, verbose_name='Текст новости')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def get_absolute_url(self):
        return reverse('news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-id']


class Documents(models.Model):
    name = models.CharField(max_length=100, verbose_name='Отображаемое имя документа')
    document = models.FileField(upload_to='documents/', verbose_name='Имя файла')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Debtors(models.Model):
    payment_order = models.IntegerField(default=0, verbose_name='№ платёжного поручения')
    personal_account = models.CharField(default='', max_length=100, verbose_name='№ лицевого счёта')
    last_paid_month = models.CharField(default='', max_length=100, verbose_name='Последний оплаченный месяц')

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'


class MainPicture(models.Model):
    picture = models.ImageField(upload_to=rename_main_picture)

    def save(self, *args, **kwargs):
        try:
            this = MainPicture.objects.all()
            for i in this:
                # print(i)
                i.delete()
        except ObjectDoesNotExist:
            pass
        super(MainPicture, self).save(*args, **kwargs)
