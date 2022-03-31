from django.shortcuts import render
from django.views import View

from .models import News, Documents, MeterReadings, Debtors


class MainView(View):

    def get(self, request):
        return render(request, 'pages/news.html')


class ElectricityTableView(View):

    def get(self, request):
        text = 'Актуальные показания электроэнергии'
        electricity = MeterReadings.objects.all()
        return render(request, 'pages/electricity.html', {'electricity': electricity, 'text': text})


class NewsView(View):

    def get(self, request):
        news = News.objects.all()
        text = 'Здесь вы можете узнать чем живет наш Малый-Петербург'

        return render(request, 'pages/news.html', {'news': news, 'text': text})


class FeedbackView(View):

    def get(self, request):
        text = 'Есть вопросы? Свяжитесь с нами'
        return render(request, 'pages/feedback.html', {'text': text})


class ContentView(View):

    def get(self, request):
        text = 'Немного о нас'
        return render(request, 'pages/about_us.html', {'text': text})


class DebtorsView(View):

    def get(self, request):
        text = 'Актуальный список должников'
        debtors = Debtors.objects.all()
        return render(request, 'pages/debtors.html', {'debtors': debtors, 'text': text})


class DocumentsView(View):

    def get(self, request):
        text = 'Список актуальных документов нашего посёлка'
        docs = Documents.objects.all()
        return render(request, 'pages/documents.html', {'docs': docs, 'text': text})


class RegisterView(View):

    def get(self, request):
        text = 'Регистрация нового пользователя'
        return render(request, 'pages/registration.html', {'text': text})


class TestView(View):

    def get(self, request):
        return render(request, 'temp/personal_area.html')