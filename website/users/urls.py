from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
]
