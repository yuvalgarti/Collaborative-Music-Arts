from django.shortcuts import redirect
from django.views import View
import json

from compositions.models import TrackInVariation, Track, Variation


class SaveTimingsView(View):
    def post(self, request, *args, **kwargs):
        js_tracks = json.loads(request.POST['timings'])
        variation_id = kwargs['variation_id']
        if Variation.objects.get(id=variation_id).creator.id == request.user.id:
            for t in js_tracks:
                py_track = Track.objects.get(track_file=js_tracks[t][1][len('/media//'):]).id
                track_in_vari = TrackInVariation.objects.get(track_id=py_track, variation_id=variation_id)
                track_in_vari.start_timing = js_tracks[t][0]
                track_in_vari.save()
        return redirect('show_variation', variation_id)
