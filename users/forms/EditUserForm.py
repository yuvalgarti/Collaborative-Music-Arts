import os
from django import forms
from . import SignUpForm
from ..functionalities import *
from django.contrib.auth.models import User


class EditUserForm(SignUpForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'password-control',
        'disabled': True
    }))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'password-control'
    }))
    password_confirmation = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'password-control'
    }))