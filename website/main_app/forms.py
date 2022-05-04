from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['name', 'email', 'message_title', 'message_text']
        widgets = {
            'message_text': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            )
        }


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'contact__form-input', 'placeholder': 'Имя'})
        self.fields['email'].widget.attrs.update({'class': 'contact__form-input', 'placeholder': 'E-mail'})
        self.fields['message_title'].widget.attrs.update({'class': 'contact__form-input', 'placeholder': 'Тема письма'})
        self.fields['message_text'].widget.attrs.update({'class': 'contact__form-area', 'placeholder': 'Текст сообщения'})

        self.fields['message_title'].label = ""
        self.fields['message_text'].label = ""
