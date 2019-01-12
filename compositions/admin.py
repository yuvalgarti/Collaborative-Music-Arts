from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Composition)
admin.site.register(models.Variation)
admin.site.register(models.Track)
