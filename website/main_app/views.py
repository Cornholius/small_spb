from django.shortcuts import render
from django.views import View

from .models import News


class MainView(View):

    def get(self, request):
        return render(request, 'pages/news.html')


class ElectricityTableView(View):

    def get(self, request):
        return render(request, 'pages/electricity.html')


class NewsView(View):

    def get(self, request):
        news = News.objects.all()
        return render(request, 'pages/news.html', {'news': news})


class FeedbackView(View):

    def get(self, request):
        return render(request, 'pages/feedback.html')