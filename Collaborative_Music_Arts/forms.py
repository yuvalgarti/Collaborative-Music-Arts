import os
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    thumbnail = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['name', 'thumbnail']