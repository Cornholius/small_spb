from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'area_number')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form__input _req",
                                                     'placeholder': 'Логин'})
        self.fields['first_name'].widget.attrs.update({'class': "form__input _req",
                                                       'placeholder': 'Аркадий'})
        self.fields['last_name'].widget.attrs.update({'class': 'form__input _req',
                                                      'placeholder': 'Паровозов'})
        self.fields['middle_name'].widget.attrs.update({'class': 'form__input _req',
                                                        'placeholder': 'Игоревич'})
        self.fields['email'].widget.attrs.update({'class': 'form__input _req _email',
                                                  'placeholder': 'example@example.ru'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form__input _req _email',
                                                         'placeholder': 'Пример: +71234567890'})
        self.fields['area_number'].widget.attrs.update({'class': 'select__header',
                                                        'placeholder': 'Выбрать № участка'})
        self.fields['password1'].widget.attrs.update({'class': 'form__input _req _email',
                                                      'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form__input _req _email',
                                                      'placeholder': 'Повторите пароль'})
        for _ in self.fields:
            self.fields[_].label = ''
            self.fields[_].help_text = ''


class LoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'menu__list-item--input-style',
                                                     'placeholder': 'Имя пользователя'})
        self.fields['password'].widget.attrs.update({'class': 'menu__list-item--input-style',
                                                     'placeholder': 'Пароль'})
        self.fields['username'].label = ""
        self.fields['password'].label = ""
