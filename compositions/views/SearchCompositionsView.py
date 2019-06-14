from django.shortcuts import redirect, render
from django.views import View

from compositions.models import Composition


class SearchCompositionsView(View):
    def get(self, request, *args, **kwargs):
        phrase = request.GET['phrase']
        compositions = Composition.objects.filter(name__icontains=phrase)
        return render(request, 'compositions/search_compositions.html', {'phrase': phrase, 'compositions': compositions})
