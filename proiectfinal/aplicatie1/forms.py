from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from aplicatie1.models import Post
from .models import Book


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']


class BookForm(forms.ModelForm):
   class Meta:
       model = Book
       fields = ['title','category','pdf', 'cover']