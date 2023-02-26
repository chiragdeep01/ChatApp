from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
import string
import random
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name+'-'+self.slug

class Message(models.Model):
    user = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='message', on_delete=models.CASCADE)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('date_added',)

class Room_Member(models.Model):
    user = models.ForeignKey(User, related_name='room_member', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='room_member', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + '-' + self.room.name
    
    def save(self, *args, **kwargs):
        exists = Room_Member.objects.filter(user = self.user, room = self.room).exists()
        if not exists:
            super().save( *args, **kwargs)

def generate_slug(sender, instance, *args, **kwargs):
    name = instance.name
    slug = slugify(name)
    while sender.objects.filter(slug = slug).exists():
        res = ''.join(random.choices(string.ascii_letters, k=4))
        name = name + res
        slug = slugify(name)
    instance.slug = slug

pre_save.connect(generate_slug, sender=Room)

    
