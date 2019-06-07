from django.shortcuts import redirect
from ..models import Variation, Track
from django.views import View
from copy import deepcopy

class ForkVariationView(View):
    def get(self, request, *args, **kwargs):
        variation_id = kwargs['variation_id']
        variation = Variation.objects.get(id=variation_id)
        old_obj = deepcopy(variation)
        old_obj.creator = request.user
        old_obj.name += '(' + str(old_obj.id) + ')'
        old_obj.id = None
        old_obj.save(user=request.user, composition_id=variation.composition.id)
        old_obj.tracks.add(*variation.tracks.all())
        return redirect('show_composition', variation.composition.id)
