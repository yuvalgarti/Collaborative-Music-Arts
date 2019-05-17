from djongo import models
from .TrackModel import Track
from .VariationModel import Variation


# Create your models here.

class TrackInVariation(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    start_timing = models.FloatField(default=0)
    stop_timing = models.FloatField(default=0)

    class Meta:
        auto_created = True
