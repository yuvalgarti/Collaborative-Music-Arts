import os
from django import forms
from ..models import *
from django.core.exceptions import ValidationError


class TrackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Track
        fields = ['instrument', 'track_file']
