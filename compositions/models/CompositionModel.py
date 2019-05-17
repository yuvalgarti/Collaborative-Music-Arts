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
