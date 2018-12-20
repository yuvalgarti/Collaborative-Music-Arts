from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CompositionForm, VariationForm, TrackForm
from .models import Composition, Variation, Track
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'compositions/index.html', {'compositions': Composition.objects.all()})


@login_required(login_url='accounts/login')
def create_composition(request):
    if request.method == 'POST':
        form = CompositionForm(request.POST)
        if form.is_valid():
            compo = form.save(commit=False)
            compo.creator = request.user
            compo.save()
            return index(request)
    else:
        form = CompositionForm()
    return render(request, 'compositions/create_composition.html', {'form': form})


@login_required(login_url='accounts/login')
def create_variation(request):
    if request.method == 'POST':
        form = VariationForm(request.POST)
        if form.is_valid():
            vari = form.save(commit=False)
            vari.creator = request.user
            vari.save()
            form.save_m2m()
            return index(request)
    else:
        form = VariationForm()
    return render(request, 'compositions/create_variation.html', {'form': form})


@login_required(login_url='accounts/login')
def create_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save(commit=False)
            track.creator = request.user
            track.save()
            return redirect('index')
    else:
        form = TrackForm()
    return render(request, 'compositions/create_track.html', {'form': form})


def show_composition(request, composition_id):
    return render(request, 'compositions/show_composition.html', context={
        'composition': Composition.objects.get(id=composition_id),
        'variations': Variation.objects.filter(composition__id=composition_id),
        'tracks': Track.objects.filter(composition__id=composition_id)
    })


def show_variation(request, variation_id):
    return render(request, 'compositions/show_variation.html', context={
            'tracks': Variation.objects.get(id=variation_id).tracks.all()
        })
