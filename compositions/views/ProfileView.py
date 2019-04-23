from django.contrib.auth.models import User
from django.shortcuts import render
from ..models import Composition
from django.views import View


class ProfileView(View):
    template_name = 'compositions/profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        return render(request, self.template_name, {
            'compositions': Composition.objects.filter(creator=User.objects.get(username=username)).order_by(
                '-created_at'),
            'username': username
        })
