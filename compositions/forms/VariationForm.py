import os
from django import forms
from ..models import *
from django.core.exceptions import ValidationError


class VariationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['tracks'] = forms.ModelMultipleChoiceField(Track.objects.filter(composition_id=self.composition_id),
                                                               widget=forms.CheckboxSelectMultiple(
                                                                   attrs={'class': 'text-left'}))

    class Meta:
        model = Variation
        fields = ['name', 'tracks']
