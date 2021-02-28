from django.shortcuts import render, HttpResponse
from datetime import datetime
from chats.models import Signin
from django.contrib import messages

# Create your views here.
def index_1(request):
    return render(request, "index_1.html")

def description(request):
    return render(request, "description.html")

def aboutus(request):
    return render(request, "aboutus.html")

def signin(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        signin = Signin(fname=fname, lname=lname, username=username, password=password, date=datetime.today())
        signin.save()
        messages.success(request, 'you have signed up successfully')
    return render(request, "signin.html")

def login(request):
    return render(request, "login.html")
