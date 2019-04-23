from django.shortcuts import render, redirect
from ..forms import CompositionForm
from django.views import View


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
            return redirect('show_composition', composition_id=compo.id)
        return render(request, self.template_name, {'form': form})
