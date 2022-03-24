from django.shortcuts import render
from django.views import View

from .models import News, Documents, MeterReadings, Debtors


class MainView(View):

    def get(self, request):
        return render(request, 'pages/news.html')


class ElectricityTableView(View):

    def get(self, request):
        electricity = MeterReadings.objects.all()
        return render(request, 'pages/electricity.html', {'electricity': electricity})


class NewsView(View):

    def get(self, request):
        news = News.objects.all()
        return render(request, 'pages/news.html', {'news': news})


class FeedbackView(View):

    def get(self, request):
        return render(request, 'pages/feedback.html')


class ContentView(View):

    def get(self, request):
        return render(request, 'pages/about_us.html')


class DebtorsView(View):

    def get(self, request):
        debtors = Debtors.objects.all()
        return render(request, 'pages/debtors.html', {'debtors': debtors})


class DocumentsView(View):

    def get(self, request):
        docs = Documents.objects.all()
        return render(request, 'pages/documents.html', {'docs': docs})
