from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('create_composition', login_required(views.CreateCompositionView.as_view()), name='create_composition'),
    url(r'^create_variation/(?P<composition_id>[0-9]+)$', login_required(views.CreateVariationView.as_view()),
        name='create_variation'),
    url(r'^create_track/(?P<composition_id>[0-9]+)$',
        login_required(views.CreateTrackView.as_view()), name='create_track'),
    url(r'^composition/(?P<composition_id>[0-9]+)$', views.ShowCompositionView.as_view(), name='show_composition'),
    url(r'^variation/(?P<variation_id>[0-9]+)$', views.ShowVariationView.as_view(), name='show_variation'),
    url(r'^profile/(?P<username>[\w\-]+)$', views.ProfileView.as_view(), name='profile'),
    url(r'^delete_composition/(?P<composition_id>[0-9]+)$', login_required(views.DeleteCompositionView.as_view()),
        name='delete_composition'),
    url(r'^delete_track/(?P<track_id>[0-9]+)$', login_required(views.DeleteTrackView.as_view()),
        name='delete_track'),
    url(r'^fork_variation/(?P<variation_id>[0-9]+)$', login_required(views.ForkVariationView.as_view()),
        name='fork_variation'),
    url(r'^edit_variation/(?P<variation_id>[0-9]+)$', login_required(views.EditVariationView.as_view()),
        name='edit_variation'),
    url(r'^like/(?P<track_id>[0-9]+)$', login_required(views.LikeButtonView.as_view()), name='like_button'),
    url(r'^search_compositions', login_required(views.SearchCompositionsView.as_view()), name='search_compositions'),
    url(r'^save_timings/(?P<variation_id>[0-9]+)$', login_required(views.SaveTimingsView.as_view()), name='save_timings'),
    path('', views.IndexView.as_view(), name='index')
]
