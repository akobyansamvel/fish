from django.db import models
import json

class Fish(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    habitat = models.TextField()
    requirements = models.TextField()
    food = models.TextField()
    compatibility = models.JSONField(blank=True, null=True, default=list)
    photos_count = models.IntegerField()
    image_paths = models.JSONField()

    class Meta:
        db_table = 'fishes'
