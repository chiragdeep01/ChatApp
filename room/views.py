from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message, Room_Member
from .forms import CreateRoomForm
from django.contrib.auth.models import User

@login_required
def rooms(request):
    rooms_user = Room_Member.objects.filter(user = request.user)
    return render(request,'room/rooms.html',{'rooms_user':rooms_user})


@login_required
def room_slug(request, slug):

    if request.method=='POST' and 'add-user' in request.POST:
        username = request.POST.get('username')
        if User.objects.filter(username = username).exists():
            room = Room.objects.get(slug = slug)
            user = User.objects.get(username = username)
            Room_Member.objects.create(user = user, room = room)

    if request.method=='POST' and 'remove-user' in request.POST:
        username = request.POST.get('user')
        if User.objects.filter(username = username).exists():
            user = User.objects.get(username = username)
            room = Room.objects.get(slug = slug)
            member = Room_Member.objects.get(user = user, room = room)
            member.delete()
            if not Room_Member.objects.filter(room = room).exists():
                room.delete()
                return redirect('rooms')

    room = Room.objects.get(slug = slug)
    if Room_Member.objects.filter(user = request.user, room = room).exists():
        room_members = Room_Member.objects.filter(room = room)
        messages = Message.objects.filter(room=room)[0:25]
        return render(request,'room/room_slug.html',{'room':room,'messages':messages,'room_members':room_members})
    
    return redirect('rooms')


@login_required
def room_create(request):
    if request.method=='POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room = Room.objects.create(name=form.cleaned_data.get('name'))
            Room_Member.objects.create(user = request.user, room = room)
            return redirect('rooms')
    else:
        form = CreateRoomForm()
        
    return render(request,'room/room_create.html',{'form':form})