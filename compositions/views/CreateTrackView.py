from django.shortcuts import render, redirect
from ..forms import TrackForm
from django.views import View


class CreateTrackView(View):
    template_name = 'compositions/create_track.html'

    def get(self, request, *args, **kwargs):
        composition_id = kwargs['composition_id']
        form = TrackForm(composition_id=composition_id)
        return render(request, self.template_name, {'form': form, 'composition_id': composition_id})

    def post(self, request, *args, **kwargs):
        composition_id = kwargs['composition_id']
        form = TrackForm(request.POST, request.FILES, composition_id=composition_id)
        if form.is_valid():
            track = form.save(commit=False)
            track.save(user=request.user, composition_id=composition_id)
            return redirect('show_composition', composition_id=composition_id)
        return render(request, self.template_name, {'form': form, 'composition_id': composition_id})
