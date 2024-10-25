from .models import Client
from .models import BonusCard
from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, EmailInput

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['client_id', 'name', 'surname', 'number', 'birth', 'email']

        widgets = {
            "client_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'client_id'
            }),

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),

            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),

            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),

            "birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'type': 'date'
            }),

            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
        }


class BonusCardForm(ModelForm):
    class Meta:
        model = BonusCard
        fields = ['owner', 'card_number', 'bonus', 'expiration_date']

        widgets = {
            "owner": Select(attrs={
                'class': 'form-control',
            }),

            "card_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер карты'
            }),

            "bonus": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество бонусов'
            }),

            "expiration_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата деактивации',
                'type': 'date'
            }),

        }
        owner = forms.ModelChoiceField(queryset=Client.objects.all())

