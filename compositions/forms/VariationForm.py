import os
from django import forms
from ..models import *
from django.core.exceptions import ValidationError


class VariationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['tracks'].queryset = Track.objects.filter(composition_id=self.composition_id)

    class Meta:
        model = Variation
        fields = ['name', 'tracks']
