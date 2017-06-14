# -*- coding: utf-8 -*-

from django import forms
from posts.models import User, Post, Comment
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
        widget=forms.TextInput(attrs={'placeholder': 'tinyperson@gmail.com'})
    )
    password = forms.CharField(
        label='password',
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )


class SingUpForm(forms.ModelForm):
    email = forms.EmailField(
        label='E-Mail',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'tinyperson@gmail.com'})
    )
    password = forms.CharField(
        label='Password',
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    username = forms.CharField(
        label='Username',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    birthday = forms.DateField(
        widget=extras.SelectDateWidget(
            years=range(datetime.now().year - 100, datetime.now().year)))
    city = forms.CharField(
        label='City',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'City'})
    )
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'birthday', 'country', 'city')


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    description = forms.CharField(
        label='Description',
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Description'})
    )
    image = forms.FileField(
        label='Image',
        max_length=128
    )

    class Meta:
        model = Post
        fields = ('title', 'description', 'image')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

