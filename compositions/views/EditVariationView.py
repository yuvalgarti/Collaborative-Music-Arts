from django.shortcuts import render, redirect
from ..forms import EditVariationForm
from ..models import Variation
from django.views import View


class EditVariationView(View):
    template_name = 'compositions/edit_variation.html'

    def get(self, request, *args, **kwargs):
        variation_id = kwargs['variation_id']
        vari= Variation.objects.get(id=variation_id)
        if(vari.creator.id != request.user.id):
            return redirect('show_variation', variation_id=vari.id)
        else:
            form = EditVariationForm(variation_id=variation_id, initial={'name': vari.name})
            return render(request, self.template_name, {'form': form, 'variation_id': variation_id})

    def post(self, request, *args, **kwargs):
        variation_id = kwargs['variation_id']
        form = EditVariationForm(request.POST, variation_id=variation_id)
        if form.is_valid():
            newVari = form.save(commit=False)
            vari = Variation.objects.get(id=variation_id)
            vari.tracks.set(newVari.tracks)
            vari.save(user=request.user, composition_id=vari.composition.id)
            return redirect('show_variation', variation_id=vari.id)
        return render(request, self.template_name, {'form': form, 'variation_id': variation_id})
