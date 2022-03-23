from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.NewsView.as_view(), name='main'),
    path('electricity/', views.ElectricityTableView.as_view(), name='electricity'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('content/', views.ContentView.as_view(), name='content'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]
