from django import forms

from compositions.models.RatingModel import Rate


class RatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.composition_id = kwargs.pop('composition_id')
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rate
        fields = ['rating']
