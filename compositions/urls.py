from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from . import  views

urlpatterns = [
    path('create_composition', views.create_composition, name='create_composition'),
    path('create_variation', views.create_variation, name='create_variation'),
    path('create_track', views.create_track, name='create_track'),
    url(r'^composition/(?P<composition_id>[0-9]+)$', views.show_composition, name='show_composition'),
    url(r'^variation/(?P<variation_id>[0-9]+)$', views.show_variation, name='show_variation'),
    path('', views.index, name='index')
]
