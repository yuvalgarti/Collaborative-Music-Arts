from django.shortcuts import redirect
from ..models import Composition, Track
from django.views import View


class DeleteTrackView(View):
    def get(self, request, *args, **kwargs):
        track_id = kwargs['track_id']
        track = Track.objects.get(id=track_id)
        compo = Composition.objects.get(id=track.composition_id)
        if compo.creator.id != request.user.id:
            return redirect('show_composition', composition_id=compo.id)
        else:
            track.delete()
            return redirect('show_composition', composition_id=compo.id)
