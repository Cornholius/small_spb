from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import ContactForm
from .models import *
from users.forms import LoginForm


class MainView(View):

    def get(self, request):
        return render(request, 'pages/news.html')


class ElectricityTableView(View):

    def get(self, request):
        text = 'Актуальные показания электроэнергии'
        location = 'Показания электроэнергии'
        electricity = MeterReadings.objects.all()
        return render(request, 'pages/electricity.html', {'electricity': electricity,
                                                          'text': text,
                                                          'location': location,
                                                          'LoginForm': LoginForm})


class NewsView(View):

    def get(self, request):
        news = News.objects.all()
        text = 'Здесь вы можете узнать чем живет наш Малый-Петербург'
        location = 'Новости'
        return render(request, 'pages/news.html', {'news': news,
                                                   'text': text,
                                                   'location': location,
                                                   'LoginForm': LoginForm})


class FeedbackView(View):

    def get(self, request):
        text = 'Есть вопросы? Свяжитесь с нами'
        location = 'Обратная связь'
        return render(request, 'pages/feedback.html', {'text': text,
                                                       'location': location,
                                                       'LoginForm': LoginForm,
                                                       'ContactForm': ContactForm})

    def post(self, request):
        text = 'Ваше сообщение отправлено'
        location = 'Обратная связь'
        data = request.POST
        subject = data['message_title']
        content = f"Вам пришло новое сообщение с сайта Малый-Петербург.рф" \
                  f"\n" \
                  f"\n" \
                  f"От: {data['name']}" \
                  f"\n" \
                  f"\n" \
                  f"Тема: {data['message_title']}" \
                  f"\n" \
                  f"\n" \
                  f"Текст сообщения:" \
                  f"{data['message_text']}"
        mail_from = data['email']
        mail_to = ['y.layshkin@gmail.com']
        try:
            send_mail(subject, content, mail_from, mail_to)
        except:
            print('Сообщение не отправлено')
        return render(request, 'pages/feedback.html', {'text': text,
                                                       'location': location,
                                                       'LoginForm': LoginForm,
                                                       'ContactForm': ContactForm})



class ContentView(View):

    def get(self, request):
        text = 'Немного о нас'
        location = 'О нас'
        return render(request, 'pages/about_us.html', {'text': text,
                                                       'location': location,
                                                       'LoginForm': LoginForm})


class DebtorsView(View):

    def get(self, request):
        text = 'Актуальный список должников'
        location = 'Должники'
        debtors = Debtors.objects.all()
        return render(request, 'pages/debtors.html', {'debtors': debtors,
                                                      'location': location,
                                                      'text': text,
                                                      'LoginForm': LoginForm})


class DocumentsView(View):

    def get(self, request):
        text = 'Список актуальных документов нашего посёлка'
        location = 'Документы'
        docs = Documents.objects.all()
        return render(request, 'pages/documents.html', {'docs': docs,
                                                        'location': location,
                                                        'text': text,
                                                        'LoginForm': LoginForm})


class DeleteItemView(View):

    def get(self, request, type=None, id=None):

        item_type = {
            'documents': Documents,
            'faq': FAQ,
            'debtors': Debtors,
            'news': News,

        }

        item = item_type[type].objects.get(id=id)
        item.delete()

        return redirect(f'../../../admin/main_app/{type}/')


class FAQView(View):

    def get(self, request):
        faq = FAQ.objects.all()
        text = 'Ответы на часто задаваемые вопросы'
        location = 'Вопросы и ответы'
        return render(request, 'pages/faq.html', {'faq': faq,
                                                  'text': text,
                                                  'location': location,
                                                  'LoginForm': LoginForm})


class GalleryView(View):

    def get(self, request):
        text = 'Наши фотографии'
        location = 'Галерея'
        photos = Gallery.objects.all()
        print(photos[0])
        return render(request, 'pages/gallery.html', {'photos': photos,
                                                      'text': text,
                                                      'location': location,
                                                      'LoginForm': LoginForm})
