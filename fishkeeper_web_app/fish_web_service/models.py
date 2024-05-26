from django.db import models


class Fish(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    habitat = models.TextField()
    requirements = models.TextField()
    food = models.TextField()
    compatibility =models.JSONField(default=list)
    photos_count = models.IntegerField()
    image_paths = models.JSONField(default=list)  # Use JSONField to store image paths

    def __str__(self):
        return self.name
