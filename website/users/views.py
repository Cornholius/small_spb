from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from main_app.models import MeterReadings


class RegisterView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Регистрация нового пользователя'

    def get(self, request):
        return render(request, 'pages/registration.html', {'RegisterForm': RegisterForm,
                                                           'LoginForm': LoginForm,
                                                           'text': self.text})

    def post(self, request):
        new_user = RegisterForm(request.POST)
        # if CustomUser.objects.filter(username=request.POST.get('username')).exists():
        #     return render(request, 'blog/login_or_register.html', {'form': RegisterForm, 'text': self.text})
        if new_user.is_valid():
            new_user.save()
            username = new_user.cleaned_data.get('username')
            password = new_user.cleaned_data.get('password2')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'pages/news.html')
        else:
            messages.error(request, "Invalid data")
            return render(request, 'pages/registration.html', {'LoginForm': LoginForm, 'form': RegisterForm, 'text': new_user.errors})


class LoginView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return render(request, 'pages/news.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('news')
        else:
            error_text = 'Проверьте правильность ввода логина/пароля'
            return render(request, 'pages/news.html', {'error_text': error_text, 'LoginForm': LoginForm})


class LogoutView(View):

    def get(self, request):
        auth.logout(request)
        return redirect('news')


class LkView(View):

    def get(self, request):
        text = 'Личный кабинет'
        user = CustomUser.objects.get(username=request.user)
        meter_reading = MeterReadings.objects.get(area_number=user.area_number)
        return render(request, 'pages/lk.html', {'user': user, 'text': text, 'meter_reading': meter_reading})

