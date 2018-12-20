from django import forms
from .models import Composition


class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = ['name']
