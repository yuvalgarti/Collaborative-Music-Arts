from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CompositionForm, VariationForm, TrackForm
from .models import Composition, Variation, Track
from django.views import View


# Create your views here.
class IndexView(View):
    template_name = 'compositions/index.html'

    def get(self, request):
        context = {'compositions': Composition.objects.order_by('-created_at')}
        return render(request, self.template_name, context)


class ProfileView(View):
    template_name = 'compositions/profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        return render(request, self.template_name, {
            'compositions': Composition.objects.filter(creator=User.objects.get(username=username)).order_by(
                '-created_at'),
            'username': username
        })


class CreateCompositionView(View):
    missing_thumbnail = 'thumbnails/missing.jpg'
    template_name = 'compositions/create_composition.html'

    def get(self, request):
        form = CompositionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CompositionForm(request.POST, request.FILES)
        if form.is_valid():
            compo = form.save(commit=False)
            compo.save(user=request.user)
            return redirect('index')
        return render(request, self.template_name, {'form': form})


class CreateVariationView(View):
    template_name = 'compositions/create_variation.html'

    def get(self, request, *args, **kwargs):
        composition_id = kwargs['composition_id']
        form = VariationForm(composition_id=composition_id)
        return render(request, self.template_name, {'form': form, 'composition_id': composition_id})

    def post(self, request, *args, **kwargs):
        composition_id = kwargs['composition_id']
        form = VariationForm(request.POST, composition_id=composition_id)
        if form.is_valid():
            vari = form.save(commit=False)
            vari.save(user=request.user, composition_id=composition_id)
            form.save_m2m()
            return redirect('index')
        return render(request, self.template_name, {'form': form, 'composition_id': kwargs['composition_id']})


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
            return redirect('index')
        return render(request, self.template_name, {'form': form, 'composition_id': composition_id})


class ShowCompositionView(TemplateView):
    template_name = 'compositions/show_composition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        composition_id = kwargs['composition_id']
        context['composition'] = Composition.objects.get(id=composition_id)
        context['variations'] = Variation.objects.filter(composition__id=composition_id)
        context['tracks'] = Track.objects.filter(composition__id=composition_id)
        return context


class ShowVariationView(TemplateView):
    template_name = 'compositions/mixer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        variation_id = kwargs['variation_id']
        # context['tracks'] = Variation.objects.get(id=variation_id).tracks.all()
        context['track_in_variation'] = Variation.objects.get(id=variation_id).trackinvariation_set.all()
        context['composition'] = Variation.objects.get(id=variation_id).composition
        return context


class DeleteCompositionView(View):
    def get(self, request, *args, **kwargs):
        composition_id = kwargs['composition_id']
        compo = Composition.objects.get(id=composition_id)
        if compo.creator.id != request.user.id:
            return redirect('index')
        else:
            compo.delete()
            return redirect('index')


class DeleteTrackView(View):
    def get(self, request, *args, **kwargs):
        track_id = kwargs['track_id']
        track = Track.objects.get(id=track_id)
        compo = Composition.objects.get(id=track.composition_id)
        if compo.creator.id != request.user.id:
            return redirect('index')
        else:
            track.delete()
            return redirect('index')
