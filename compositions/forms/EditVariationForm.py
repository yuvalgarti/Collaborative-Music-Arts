import os
from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class EditVariationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.variation_id = kwargs.pop('variation_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['tracks'].queryset = Track.objects.filter(composition_id=Variation.objects.get(id=self.variation_id).composition.id)

    class Meta:
        model = Variation
        fields = ['name', 'tracks']