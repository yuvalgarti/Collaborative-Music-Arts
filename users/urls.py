from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url('accounts/signup', views.SignUpView.as_view(), name='signup'),
    url(r'^edit/(?P<username>[\w\-]+)$', login_required(views.EditUserView.as_view()), name='edit')
]
