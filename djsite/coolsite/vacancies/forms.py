from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ['posada', 'firma', 'city', 'street', 'vumogu', 'responsibilities', 'pr']
        widgets = {
            'posada': forms.TextInput(attrs={'class': 'form-input'}),
            'vumogu': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UnemployedF(forms.Form):
    priz = forms.CharField(max_length=100, label="Прізвище")
    name = forms.CharField(max_length=50, label="Ім'я")
    pobat = forms.CharField(max_length=100, label="По батькові")
    city = forms.CharField(max_length=100, label="Місто")
    street = forms.CharField(max_length=50, label="Вулиця")
    year = forms.IntegerField(label="Вік")
    nomer_phone = forms.CharField(max_length=10, label="Номер телефону")
    em = forms.EmailField(label="Email")
    special = forms.CharField(max_length=100, label="Спеціальність")
    vc = forms.ModelChoiceField(queryset=Vacancies.objects.all(), label="Вакансії")

    def clean_year(self):
        year = self.cleaned_data['year']
        if year<=14 or year>=80:
            raise ValidationError('Некоректно введено вік безробітного')

        return year

