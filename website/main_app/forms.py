from captcha.fields import CaptchaField
from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact, FAQ


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
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


class FaqForm(ModelForm):

    class Meta:
        model = FAQ
        fields = ['question']

    def __init__(self, *args, **kwargs):
        super(FaqForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class': 'faq__inp', 'placeholder': 'Задайте свой вопрос'})