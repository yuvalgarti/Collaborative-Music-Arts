from django import forms
from .models import Composition, Variation, Track


class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = ['name']


class VariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = ['name', 'composition', 'tracks']


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['instrument', 'composition', 'track_file']
