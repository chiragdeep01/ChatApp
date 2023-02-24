from django.urls import path
from . import views
# from django.contrib.auth import views as authviews
urlpatterns = [
    path('',views.rooms,name='rooms'),
    path('<slug:slug>',views.room_slug,name='room_slug'),
]