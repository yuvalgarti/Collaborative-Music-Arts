from django.shortcuts import redirect
from ..models import Composition
from django.views import View


class DeleteCompositionView(View):
    def get(self, request, *args, **kwargs):
        composition_id = kwargs['composition_id']
        compo = Composition.objects.get(id=composition_id)
        if compo.creator.id != request.user.id:
            return redirect('index')
        else:
            compo.delete()
            return redirect('index')
