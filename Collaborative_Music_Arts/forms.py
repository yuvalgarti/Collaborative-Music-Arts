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
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-control'

    }))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self['password_confirmation'].data
        if len(password) < 8:
            raise ValidationError('Password too short')
        if len(password) != len(password_confirmation):
            raise ValidationError('Passwords don\'t match')
        if False in [password[i] == password_confirmation[i] for i in range(len(password))]:
            raise ValidationError('Passwords don\'t match')
        return password


    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class EditUserForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'password-control',
        'disabled': True
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
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'password-control'
    }))
    password_confirmation = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'password-control'
    }))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self['password_confirmation'].data
        if len(password) == 0 and len(password_confirmation) ==0:
            return password
        if len(password) < 8:
            raise ValidationError('Password too short')
        if len(password) != len(password_confirmation):
            raise ValidationError('Passwords don\'t match')
        if False in [password[i] == password_confirmation[i] for i in range(len(password))]:
            raise ValidationError('Passwords don\'t match')
        return password


    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']