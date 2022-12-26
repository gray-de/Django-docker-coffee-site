import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Post


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Эл. почта')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Название')
    content = forms.Textarea()

    # def __init__(self, user_info, *args, **kwargs):
    #     self.user_info = user_info
    #     super().__init__(*args, **kwargs)
    #
    # def clean(self):
    #     """Используем, если не убираем из формы, а просто даем возможность его не вводить blank=True"""
    #     cleaned_data = super().clean()
    #     cleaned_data['account'] = self.user_info
    #     return cleaned_data

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'category')

