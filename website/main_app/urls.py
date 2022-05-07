from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsView.as_view(), name='main'),
    path('delete/<type>/<id>/', views.DeleteItemView.as_view(), name='delete'),
    path('electricity/', views.ElectricityTableView.as_view(), name='electricity'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('content/', views.ContentView.as_view(), name='content'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('debstors/', views.DebtorsView.as_view(), name='debstors'),
    path('documents/', views.DocumentsView.as_view(), name='documents'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
]
