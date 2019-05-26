import os
from django import forms
from ..models import *
from django.core.exceptions import ValidationError


class CompositionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    thumbnail = forms.ImageField(required=False)

    class Meta:
        model = Composition
        fields = ['name', 'thumbnail']
