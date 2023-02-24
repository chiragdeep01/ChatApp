from django.db import models

class Room(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True)
