from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import time

# Create your views here.
def user_login(request):
    print("current time", time.strftime("%H:%M:%S", time.localtime()))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        print(username, password)
        employee = authenticate(request, username=username, password=password)
        if employee == None:
            print("yes")
        print("yes it is: ", employee.is_authenticated)
        if employee is not None:
            print("employee is not none")
            login(request, employee)
            return redirect('home')
    context = {}
    return render(request, "login.html", context)

def home(request):
    return render(request, "home.html", {})