from django.contrib import auth, messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from main_app.models import MeterReadings, News


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
        news = News.objects.all()
        text = 'Здесь вы можете узнать чем живет наш Малый-Петербург'
        location = 'Новости'

        if new_user.is_valid():
            new_user.save()
            username = new_user.cleaned_data.get('username')
            password = new_user.cleaned_data.get('password2')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'pages/news.html', {'news': news,
                                                       'text': text,
                                                       'location': location,
                                                       'LoginForm': LoginForm})
        else:
            messages.error(request, "Invalid data")
            errors_list = []
            for i in new_user.errors:
                errors_list.append(new_user.errors[i].as_text())
            errors = '<br>'.join(errors_list)
            return render(request, 'pages/registration.html', {'LoginForm': LoginForm,
                                                               'RegisterForm': RegisterForm,
                                                               'text': errors})


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
            return render(request, 'pages/news.html', {'error_text': error_text,
                                                       'LoginForm': LoginForm})


class LogoutView(View):

    def get(self, request):
        auth.logout(request)
        return redirect('news')


class LkView(View):

    def get(self, request):
        text = 'Личный кабинет'
        user = CustomUser.objects.get(username=request.user)
        meter_reading = MeterReadings.objects.get(area_number=user.area_number)
        return render(request, 'pages/lk.html', {'user': user,
                                                 'text': text,
                                                 'meter_reading': meter_reading})

    def post(self, request):
        text = 'Личный кабинет'
        user = CustomUser.objects.get(username=request.user)
        meter_reading = MeterReadings.objects.get(area_number=user.area_number)
        current_pass = request.POST['currentPassword']
        new_pass1 = request.POST['newPassword1']
        new_pass2 = request.POST['newPassword2']
        if check_password(current_pass, user.password) and new_pass1 == new_pass2:
            user.set_password(new_pass1)
            user.save()
            flag = 'confirm'
        else:
            flag = 'fail'

        return render(request, 'pages/lk.html', {'user': user,
                                                 'text': text,
                                                 'meter_reading': meter_reading,
                                                 flag: True})
