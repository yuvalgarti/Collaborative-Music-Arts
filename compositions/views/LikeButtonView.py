from django.shortcuts import redirect
from django.views import View

from compositions.models import Track
from compositions.models.RatingModel import Rate


class LikeButtonView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        track_id = kwargs['track_id']
        track = Track.objects.get(id=track_id)
        if Rate.objects.filter(user_id=user.id, track_id=track_id).exists():
            rate = Rate.objects.get(user_id=user.id, track_id=track_id)
            rate.delete()
        else:
            rate = Rate(user_id=user.id, track_id=track_id)
            rate.save()
        return redirect('show_composition', track.composition.id)
