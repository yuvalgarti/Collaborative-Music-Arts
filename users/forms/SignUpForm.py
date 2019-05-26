import os
from django import forms
from ..functionalities import *
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'password-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'password-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'password-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'password-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-control'
    }))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-control'

    }))

    def clean_password(self):
        return checkPassword(self.cleaned_data.get('password'), self['password_confirmation'].data)


    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
