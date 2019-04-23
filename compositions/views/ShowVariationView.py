from django.views.generic import TemplateView
from ..models import Variation


class ShowVariationView(TemplateView):
    template_name = 'compositions/mixer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        variation_id = kwargs['variation_id']
        # context['tracks'] = Variation.objects.get(id=variation_id).tracks.all()
        context['track_in_variation'] = Variation.objects.get(id=variation_id).trackinvariation_set.all()
        context['composition'] = Variation.objects.get(id=variation_id).composition
        return context
