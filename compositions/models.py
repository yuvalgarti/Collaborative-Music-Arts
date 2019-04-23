from djongo import models
from django.contrib.auth import get_user_model

# Create your models here.
class Composition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails')
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        missing_thumbnail = 'thumbnails/missing.jpg'
        user = kwargs.pop('user')
        self.creator = user
        if not self.thumbnail:
            self.thumbnail = missing_thumbnail
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + ' - ' + self.creator.username


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


class Variation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track, through='TrackInVariation')

    def save(self, *args, **kwargs):
        user = kwargs.pop('user')
        composition_id = kwargs.pop('composition_id')
        self.creator = user
        self.composition = Composition.objects.get(id=composition_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + ' (' + str(self.composition) + ') - ' + self.creator.username


class TrackInVariation(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    start_timing = models.FloatField(default=0)
    stop_timing = models.FloatField(default=0)

    class Meta:
        auto_created = True
