from django.contrib import auth
from django.shortcuts import render
from django.views import View
from .models import CustomUser
from .forms import RegisterForm


class RegisterView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_button = 'Зарегистрироваться и войти'

    def get(self, request):
        return render(request, 'pages/registration.html', {'form': RegisterForm})

    def post(self, request):
        new_user = RegisterForm(request.POST)

        if CustomUser.objects.filter(username=request.POST.get('username')).exists():
            error_text = 'Пользователь с таким логином уже существует'
            return render(request, 'blog/login_or_register.html', {'form': RegisterForm,
                                                                   'error': error_text})
        if new_user.is_valid():
            new_user.save()
            username = new_user.cleaned_data.get('username')
            password = new_user.cleaned_data.get('password2')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'pages/news.html')
        else:
            return render(request, 'pages/registration.html', {'form': RegisterForm})

# class LoginView(View):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.text_button = 'Войти'
#         self.error_text = 'Неверный логин или пароль'
#
#     def get(self, request):
#         return render(request, 'blog/login_or_register.html', {'form': LoginForm, 'button': self.text_button})
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('../')
#         else:
#             return render(request, 'blog/login_or_register.html', {'error': self.error_text,
#                                                                    'form': LoginForm,
#                                                                    'button': self.text_button})
#
#
# class LogoutView(View):
#
#     def get(self, request):
#         auth.logout(request)
#         return redirect('../login')
