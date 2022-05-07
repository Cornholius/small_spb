from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('lk/', views.LkView.as_view(), name='lk'),
]
