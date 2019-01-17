from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('create_composition', login_required(views.CreateCompositionView.as_view()), name='create_composition'),
    url(r'^create_variation/(?P<composition_id>[0-9]+)$', login_required(views.CreateVariationView.as_view()),
        name='create_variation'),
    url(r'^create_track/(?P<composition_id>[0-9]+)$',
        login_required(views.CreateTrackView.as_view(), login_url='/accounts/login'), name='create_track'),
    url(r'^composition/(?P<composition_id>[0-9]+)$', views.ShowCompositionView.as_view(), name='show_composition'),
    url(r'^variation/(?P<variation_id>[0-9]+)$', views.show_variation, name='show_variation'),
    url(r'^profile/(?P<username>[\w\-]+)$', views.ProfileView.as_view(), name='profile'),
    path('', views.IndexView.as_view(), name='index')
]
