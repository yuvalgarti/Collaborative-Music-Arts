from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CompositionForm, VariationForm, TrackForm
from .models import Composition, Variation, Track
from django.views import View


# Create your views here.
class IndexView(View):
    template_name = 'compositions/index.html'
    context = {'compositions': Composition.objects.order_by('-created_at')}

    def get(self, request):
        return render(request, self.template_name, self.context)


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
            compo.creator = request.user
            if not compo.thumbnail:
                compo.thumbnail = self.missing_thumbnail
            compo.save()
            return redirect('index')


@login_required(login_url='/accounts/login')
def create_variation(request, composition_id):
    if request.method == 'POST':
        form = VariationForm(request.POST, composition_id=composition_id)
        if form.is_valid():
            vari = form.save(commit=False)
            vari.creator = request.user
            vari.composition = Composition.objects.get(id=composition_id)
            vari.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = VariationForm(composition_id=composition_id)
    return render(request, 'compositions/create_variation.html', {'form': form, 'composition_id': composition_id})


@login_required(login_url='/accounts/login')
def create_track(request, composition_id):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES, composition_id=composition_id)
        if form.is_valid():
            track = form.save(commit=False)
            track.creator = request.user
            track.composition = Composition.objects.get(id=composition_id)
            track.save()
            return redirect('index')
    else:
        form = TrackForm(composition_id=composition_id)
    return render(request, 'compositions/create_track.html', {'form': form, 'composition_id': composition_id})


def show_composition(request, composition_id):
    return render(request, 'compositions/show_composition.html', context={
        'composition': Composition.objects.get(id=composition_id),
        'variations': Variation.objects.filter(composition__id=composition_id),
        'tracks': Track.objects.filter(composition__id=composition_id)
    })


def show_variation(request, variation_id):
    return render(request, 'compositions/show_variation.html', context={
        'tracks': Variation.objects.get(id=variation_id).tracks.all(),
        'track_in_variation': Variation.objects.get(id=variation_id).trackinvariation_set.all(),
        'composition': Variation.objects.get(id=variation_id).composition
    })
