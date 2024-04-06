from .models import Data
from django.forms import TextInput, ModelForm

class LogForm(ModelForm):
    class Meta:
        model = Data
        fields = ["login", "password"]
        widgets = {
            "login": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Логин"
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "type": "password",
                "placeholder": "Пароль"
            })
        }
class RegForm(ModelForm):
    class Meta:
        model = Data
        fields = ["login", "password", "name", "surname"]
        widgets = {
            "login": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Логин"
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "type": "password",
                "placeholder": "Пароль"
            }),
            "name": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Имя"
            }),
            "surname": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Фамилию"
            })
        }
