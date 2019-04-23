from django.shortcuts import render
from ..models import Composition
from django.views import View


class IndexView(View):
    template_name = 'compositions/index.html'

    def get(self, request):
        context = {'compositions': Composition.objects.order_by('-created_at')}
        return render(request, self.template_name, context)
