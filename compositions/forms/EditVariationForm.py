import os
from django import forms

from compositions.forms import VariationForm
from ..models import *
from django.core.exceptions import ValidationError

class EditVariationForm(VariationForm):
    def __init__(self, *args, **kwargs):
        self.variation_id = kwargs.pop('variation_id')
        super.composition_id = Variation.objects.get(id=self.variation_id).composition_id

