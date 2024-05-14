from django.db import models


class Fishes(models.Model):
    # id = models.AutoField()  # Primary key
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    habitat = models.TextField(blank=True, max_length=200)
    requirements = models.TextField(blank=True)
    food = models.TextField(blank=True)
    compatibility = models.JSONField(blank=True, default={})
    photos_count = models.IntegerField()

    def __str__(self):
        return self.name
