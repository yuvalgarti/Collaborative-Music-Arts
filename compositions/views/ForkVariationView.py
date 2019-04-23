from django.shortcuts import redirect
from ..models import Composition, Variation
from django.views import View


class ForkVariationView(View):
    def get(self, request, *args, **kwargs):
        variation_id = kwargs['variation_id']
        variation = Variation.objects.get(id=variation_id)
        variation.id = None
        variation.creator = request.user
        variation.save(user=request.user, composition_id=variation.composition.id)
        return redirect('show_composition', variation.composition.id)
