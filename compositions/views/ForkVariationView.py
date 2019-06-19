from django.shortcuts import redirect
from ..models import Variation, Track, TrackInVariation
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
        for i in range(old_obj.tracks.count()):
            track_in_vari = TrackInVariation.objects.get(track_id=old_obj.tracks.all()[i].id, variation_id=old_obj.id)
            track_in_vari.start_timing = TrackInVariation.objects.get(track_id=old_obj.tracks.all()[i].id,
                                                                      variation_id=variation.id).start_timing
            track_in_vari.save()
        return redirect('show_composition', variation.composition.id)
