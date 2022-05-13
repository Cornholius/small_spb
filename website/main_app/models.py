from pathlib import Path
from PIL import Image
from tinymce import models as tinymce_models
from .utils import rename_main_picture
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class MeterReadings(models.Model):

    area_number = models.CharField(max_length=60, verbose_name='№ участка')
    personal_account = models.CharField(max_length=60, verbose_name='№ лицевого счета', blank=True, null=True)
    current_day = models.IntegerField(default=0, verbose_name='текущие показания день', blank=True, null=True)
    current_night = models.IntegerField(default=0, verbose_name='текущие показания ночь', blank=True, null=True)

    class Meta:
        verbose_name = 'Показания электро энергии'
        verbose_name_plural = 'Показания электро энергии'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    text = tinymce_models.HTMLField(max_length=8000, verbose_name='Текст новости')
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
    debtor_fio = models.CharField(default='', max_length=200, verbose_name='ФИО Собственника', blank=True, null=True)
    last_paid_month = models.CharField(default='', max_length=100, verbose_name='Последний оплаченный месяц',
                                       blank=True, null=True)

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'


class MainPicture(models.Model):
    BASE_DIR = Path(__file__).resolve().parent.parent
    picture = models.ImageField(upload_to=rename_main_picture, verbose_name='Фото главного экрана')

    def __str__(self):
        return 'Фото главной страницы'

    class Meta:
        verbose_name = 'Изменяемый объект'
        verbose_name_plural = 'Изменяемые объекты'


class FAQ(models.Model):
    question = models.CharField(default='', max_length=500, verbose_name='Вопрос')
    answer = models.TextField(default='', max_length=3000, verbose_name='Ответ', blank=True, null=True)
    on_top = models.BooleanField(verbose_name='Отображать в начале списка', default=False)

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ['id']

    def __str__(self):
        return self.question


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото галереи'
        verbose_name_plural = 'Фото галереи'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        _Max_size = 1080
        super(Gallery, self).save(*args, **kwargs)
        filepath = self.photo.path
        width = self.photo.width
        height = self.photo.height
        max_size = max(width, height)
        image = Image.open(filepath)
        image = image.resize(
            (round(width / max_size * _Max_size),
             round(height / max_size * _Max_size)),
            Image.ANTIALIAS
        )
        image.save(filepath)

    def admin_image(self):
        return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="300"/></a>'.format(self.photo.url))
    admin_image.allow_tags = True
    admin_image.short_description = 'Превью'

    def __str__(self):
        return self.photo.name


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(max_length=200, verbose_name='Почтовый адрес')
    message_title = models.CharField(max_length=200, verbose_name='Заголовок')
    message_text = models.TextField(max_length=3000, verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-id']

    def __str__(self):
        return self.email
