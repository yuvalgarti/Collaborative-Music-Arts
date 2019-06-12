from django.shortcuts import render, redirect
from ..forms import  VariationForm
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
            print(vari.tracks.all())
            form = VariationForm(composition_id=vari.composition_id, initial={
                'name': vari.name, 'tracks': vari.tracks.all()})
            return render(request, self.template_name, {'form': form, 'variation_id': variation_id})

    def post(self, request, *args, **kwargs):
        variation_id = kwargs['variation_id']
        composition_id = Variation.objects.get(id=variation_id).composition_id
        form = VariationForm(request.POST, composition_id=composition_id)
        if form.is_valid():
            vari = Variation.objects.get(id=variation_id)
            vari.tracks.set(form.cleaned_data['tracks'])
            vari.save(user=request.user, composition_id=vari.composition.id)
            return redirect('show_variation', variation_id=vari.id)
        return render(request, self.template_name, {'form': form, 'variation_id': variation_id})