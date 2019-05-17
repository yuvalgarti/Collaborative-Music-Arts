from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from ..forms import SignUpForm
from django.contrib.auth.models import User
from django.views import View


# Create your views here.
class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], email=request.POST['email'],
                                            password=request.POST['password'], first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'])
            user.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
