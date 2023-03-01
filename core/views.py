from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login
from room.models import Room_Member,Room
def frontpage(request):
    return render(request,"core/frontpage.html")

def signupPage(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            room = Room.objects.get(slug = 'welcome')
            Room_Member.objects.create(user = user, room = room)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request,'core/signup.html',{'form':form})
