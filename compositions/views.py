from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .Forms import CompositionForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'compositions/index.html')


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
    return render(request, 'compositions/Create_Composition.html', {'form': form})
