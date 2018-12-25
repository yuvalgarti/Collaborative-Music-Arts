from django import forms
from .models import Composition, Variation, Track


class CompositionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Composition
        fields = ['name', 'thumbnail']


class VariationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)

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
