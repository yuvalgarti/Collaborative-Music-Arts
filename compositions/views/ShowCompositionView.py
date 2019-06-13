from django.views.generic import TemplateView

from compositions.models.RatingModel import Rate
from ..models import Composition, Variation, Track


class ShowCompositionView(TemplateView):
    template_name = 'compositions/show_composition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        composition_id = kwargs['composition_id']
        context['composition'] = Composition.objects.get(id=composition_id)
        context['variations'] = Variation.objects.filter(composition__id=composition_id)
        context['tracks'] = Track.objects.filter(composition__id=composition_id)
        for t in context['tracks']:
            t.liked_users = []
            t.likes = Rate.objects.filter(track_id=t.id).count()
            for rater in Rate.objects.filter(track_id=t.id):
                t.liked_users.append(rater.user)
        return context
