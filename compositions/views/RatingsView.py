from django.shortcuts import render
from ..models import Composition
from django.views import View


class RatingView(View):
    template_name = 'compositions/rating.html'

    def get(self, request):
        context = {'compositions': Composition.objects.order_by('-created_at')}
        return render(request, self.template_name, context)
