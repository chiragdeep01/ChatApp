from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    user = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='message', on_delete=models.CASCADE)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('date_added',)