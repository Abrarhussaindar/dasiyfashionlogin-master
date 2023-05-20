from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import time
from datetime import datetime
from django.contrib.auth.decorators import login_required

# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         time_sec += 1

#     print("stop")

# countdown(1)


# login_times = []
# logout_times = []


def user_login(request):
    print("current time", time.strftime("%H:%M:%S", time.localtime()))
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('Password')
        print(username, password)
        employee = authenticate(request, username=username, password=password)

        

        if employee is not None:
            print("employee is not none")
            employee.login_counter += 1
            login(request, employee)
            employe_counter = employee.login_counter
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            employee.login_list.append(current_time)
            employee.intime = employee.login_list[-1]
            print("employee intime from db:", employee.intime)
            employee.save()
            print("login counts: ",employe_counter)
            print("employee login list from db: ",employee.login_list)
            return redirect('home')
            
    context = {}
    return render(request, "login.html", context)


@login_required
def user_logout(request):
    emp = request.user
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    emp.logout_list.append(current_time)
    emp.out_time = emp.logout_list[-1]
    emp.logout_counter += 1
    emp.save()
    print("employee logout list from db: ",emp.login_list)
    logout(request)
    return redirect('user_login')

def create_new_user(request):
    return render(request, "register.html", {})

# @login_required
def home(request):
    emp = request.user
    context = {
        "emp": emp,
    }
    return render(request, "home.html", context)
