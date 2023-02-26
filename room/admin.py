from django.contrib import admin

from .models import Room,Message, Room_Member

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Room_Member)
