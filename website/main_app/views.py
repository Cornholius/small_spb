from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm, FaqForm
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
        feedback = ContactForm(request.POST)

        if feedback.is_valid():
            feedback.save()
            return render(request, 'pages/feedback.html', {'text': text,
                                                           'location': location,
                                                           'LoginForm': LoginForm,
                                                           'ContactForm': ContactForm})

        #   Если нужна отправка формы на почту:
        #   (не забудь раскоментить код в settings)

        # data = request.POST
        # subject = data['message_title']
        # content = f"Вам пришло новое сообщение с сайта Малый-Петербург.рф" \
        #           f"\n" \
        #           f"\n" \
        #           f"От: {data['name']}" \
        #           f"\n" \
        #           f"\n" \
        #           f"Тема: {data['message_title']}" \
        #           f"\n" \
        #           f"\n" \
        #           f"Текст сообщения:" \
        #           f"{data['message_text']}"
        # mail_from = data['email']
        # mail_to = ['y.layshkin@gmail.com']
        # try:
        #     send_mail(subject, content, mail_from, mail_to)
        # except:
        #     print('Сообщение не отправлено')
        # return render(request, 'pages/feedback.html', {'text': text,
        #                                                'location': location,
        #                                                'LoginForm': LoginForm,
        #                                                'ContactForm': ContactForm})


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
        all_questions = FAQ.objects.all()
        faq_on_top = []
        faq = []
        text = 'Ответы на часто задаваемые вопросы'
        location = 'Вопросы и ответы'

        for question in all_questions:
            if question.on_top:
                faq_on_top.append(question)
            else:
                faq.append(question)
        return render(request, 'pages/faq.html', {'faq_on_top': faq_on_top,
                                                  'faq': faq,
                                                  'text': text,
                                                  'FaqForm': FaqForm,
                                                  'location': location,
                                                  'LoginForm': LoginForm})

    def post(self, request):
        question = FaqForm(request.POST)
        if question.is_valid():
            question.save()
        return redirect('faq')


class GalleryView(View):

    def get(self, request):
        text = 'Наши фотографии'
        location = 'Галерея'
        photos = Gallery.objects.all()
        return render(request, 'pages/gallery.html', {'photos': photos,
                                                      'text': text,
                                                      'location': location,
                                                      'LoginForm': LoginForm})
