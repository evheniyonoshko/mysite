# -*- coding: utf-8 -*-

from django import forms
from posts.models import User
from mysite import settings
from django.forms import extras
from datetime import datetime

__author__ = 'Yevhenii Onoshko'


class UserAdminForm(forms.ModelForm):
    user_permissions = forms.SelectMultiple(
        attrs={
            'class': 'select2'
        }
    )

    class Meta:
        model = User
        exclude = ('last_login', 'password')


class LoginForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(
        label='E-Mail',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'tinyperson@gmail'})
    )
    password = forms.CharField(
        label='password',
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )


class SingUpFrom(forms.ModelForm):
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)
    birthday = forms.DateField(widget=extras.SelectDateWidget(years=range(datetime.now().year - 100, datetime.now().year)))

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'birthday', 'country', 'city')

