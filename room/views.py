from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from .forms import CreateRoomForm

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request,'room/rooms.html',{'rooms':rooms})

@login_required
def room_slug(request, slug):
    room = Room.objects.get(slug = slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request,'room/room_slug.html',{'room':room,'messages':messages})

@login_required
def room_create(request):
    if request.method=='POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = CreateRoomForm()
    return render(request,'room/room_create.html',{'form':form})