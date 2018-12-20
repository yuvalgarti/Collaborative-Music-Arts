from django.contrib import admin
from django.urls import path
from django.urls import include
from . import  views

urlpatterns = [
    path('create_composition', views.create_composition, name='create_composition'),
    path('', views.index, name='index')
]
