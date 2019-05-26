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
        if form.is_valid():
            newUser = form.save(commit=False)
            user = User.objects.get(username=kwargs['username'])
            return editUser(user,newUser)
        return redirect('edit', kwargs['username'])
