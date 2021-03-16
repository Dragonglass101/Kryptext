from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from chats.models import Friend
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from chats.form import CreateUserForm
from django.contrib.auth.models import User
from datetime import datetime
import json


# Create your views here.
def index_1(request):
    return render(request, "index_1.html")

def description(request):
    return render(request, "description.html")

def aboutus(request):
    return HttpResponse("this is the about page")

def signin(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created!')
            return redirect('login')
            
    context = {'form':form}
    return render(request, "signin.html", context)

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, "login.html", context)

def index_2(request):
    user_all = User.objects.values()
    lst = []

    i = 1
    while(i<len(user_all)):
        lst.append(user_all[i]['username'])
        i += 1
    context = {"users":lst}
    return render(request, 'index_2.html', context)

def compose(request):
    if request.method == "POST" and 'send' in request.POST:
        messages.success(request, "Your message has been sent")
        from Drive_Kryp_Interaction import butt_send
        
        butt_send.send_run()
        
        # import sys
        # sys.path.insert(0, '../Drive_Kryp_Interaction')
        

        return render(request, 'compose.html')

    return render(request, "compose.html")

def chat_history(request):
    return render(request, 'chat_history.html')

def test(request):
    return render(request, 'test.html')