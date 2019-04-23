import os
from django import forms
from django.core.exceptions import ValidationError
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
    re_type_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-control'
    }))



    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','re_type_password']