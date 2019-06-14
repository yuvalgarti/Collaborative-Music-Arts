
from djongo import models
from django.contrib.auth import get_user_model

from .TrackModel import Track


class Rate(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
