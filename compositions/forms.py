import os
from django import forms
from .models import Composition, Variation, Track
from django.core.exceptions import ValidationError


class CompositionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    thumbnail = forms.ImageField(required=False)

    class Meta:
        model = Composition
        fields = ['name', 'thumbnail']


class VariationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['tracks'].queryset = Track.objects.filter(composition_id=self.composition_id)

    class Meta:
        model = Variation
        fields = ['name', 'tracks']


class TrackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Track
        fields = ['instrument', 'track_file']
