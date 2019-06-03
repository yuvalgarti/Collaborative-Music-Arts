from djongo import models
from django.contrib.auth import get_user_model
from .CompositionModel import Composition
from .TrackModel import Track


# Create your models here.

class Variation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track, through='TrackInVariation')

    def copy_variation(self, variation):
        self.name = variation.name
        self.creator = variation.creator
        self.composition = variation.composition
        self.tracks.set(variation.tracks)

    def save(self, *args, **kwargs):
        user = kwargs.pop('user')
        composition_id = kwargs.pop('composition_id')
        self.creator = user
        self.composition = Composition.objects.get(id=composition_id)
        super().save(*args, **kwargs)

#    def __str__(self):
 #       return self.name + ' (' + str(self.composition) + ') - ' + self.creator.username