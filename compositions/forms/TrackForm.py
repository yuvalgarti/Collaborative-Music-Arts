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

    def clean_file(self):
        file = self.cleaned_data.get("track_file", False)
        filetype = magic.from_buffer(file.read())
        if not "XML" in filetype:
            raise ValidationError("File is not XML.")
        return file
