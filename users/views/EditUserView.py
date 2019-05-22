from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from ..forms import EditUserForm
from django.contrib.auth.models import User
from django.views import View
from ..functionalities import *


# Create your views here.
class EditUserView(View):
    template_name = 'registration/editinfo.html'

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        if request.user == user:
            form = EditUserForm(initial={'username': user.username,
                                         'first_name': user.first_name,
                                         'last_name': user.last_name,
                                         'email': user.email})
            return render(request, self.template_name, {
                'username': username,
                'form': form
            })
        else:
            return redirect('index')

    def post(self, request, *args, **kwargs):
        form = EditUserForm(request.POST, request.FILES)
        redirection = redirect('edit', kwargs['username'])
        if form.is_valid():
            newUser = form.save(commit=False)
            user = User.objects.get(username=kwargs['username'])
            user.__setattr__('email',newUser.email)
            user.__setattr__('first_name', newUser.first_name)
            user.__setattr__('last_name', newUser.last_name)
            if len(newUser.password) > 0:
                user.set_password(newUser.password)
                redirection = redirect('login')
            else:
                redirection = redirect('profile', username=kwargs['username'])
            user.save()
        return redirection
