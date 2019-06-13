from djongo import models
from django.contrib.auth import get_user_model


from .CompositionModel import Composition


class Track(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    instrument = models.CharField(max_length=100)
    composition = models.ForeignKey(Composition, on_delete=models.DO_NOTHING)
    track_file = models.FileField(upload_to='tracks')

    def save(self, *args, **kwargs):
        user = kwargs.pop('user')
        composition_id = kwargs.pop('composition_id')
        self.creator = user
        self.composition = Composition.objects.get(id=composition_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.instrument + ' - ' + self.creator.username
