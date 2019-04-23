from django.shortcuts import render, redirect
from ..forms import VariationForm
from django.views import View


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
            return redirect('show_variation', variation_id=vari.id)
        return render(request, self.template_name, {'form': form, 'composition_id': kwargs['composition_id']})
