from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('create_composition', views.create_composition, name='create_composition'),
    url(r'^create_variation/(?P<composition_id>[0-9]+)$', views.create_variation, name='create_variation'),
    url(r'^create_track/(?P<composition_id>[0-9]+)$', views.create_track, name='create_track'),
    url(r'^composition/(?P<composition_id>[0-9]+)$', views.show_composition, name='show_composition'),
    url(r'^variation/(?P<variation_id>[0-9]+)$', views.show_variation, name='show_variation'),
    url(r'^profile/(?P<username>[\w\-]+)$', views.profile, name='profile'),
    path('', views.IndexView.as_view(), name='index')
]
