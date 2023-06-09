from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import time
from datetime import datetime
from django.contrib.auth.decorators import login_required


def user_login(request):
    print("current time", time.strftime("%H:%M:%S", time.localtime()))
    department_categories = ["Management/Admin",'Operations','Marketing','Sales','IT' ]
            # dict(department = url="https://www.digitaldaisy.net"),
            # dict(department =url="https://www.digitaldaisy.net"),
            # dict(department =url="https://www.digitaldaisy.net"),
            # dict(department =url="https://www.digitaldaisy.net"),
            # dict(department = url="https://www.digitaldaisy.net")
      
    
    # for i in range(len(department_categories)):
    #     print(department_categories[i]["department"],department_categories[i]["url"])

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        department = request.POST.get('department')
        print(username, password)
        employee = authenticate(request,department=department, username=username, password=password)
        print("employee authenticed: ",employee.is_authenticated)
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
            # return redirect('https://digitaldaisy.co.in/daisyfashion/')
            
    context = {
        "department_categories": department_categories
    }
    return render(request, "login.html", context)


@login_required
def user_logout(request):
    emp = request.user

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    emp.logout_list.append(current_time)
    emp.out_time = emp.logout_list[-1]

    t1 = datetime.strptime(emp.intime, "%H:%M:%S")
    t2 = datetime.strptime(emp.out_time, "%H:%M:%S")
    emp.duration_time = t2 - t1
    print("user login duration time at logout: ", emp.duration_time)
    emp.duration_list.append(str(emp.duration_time))
    print("user login duration list at logout: ", emp.duration_list[-1])
    emp.logout_counter += 1
    emp.save()
    # print("employee logout list from db: ",emp.login_list)
    logout(request)
    return redirect('login')

def create_new_user(request):
    form = CreateEmployee()
    if request.method  == 'POST':
        form = CreateEmployee(request.POST)
        print(form.is_valid())
        # print(form.cleaned_data.get('email'))
        if form.is_valid():
            form.save()
            # print(form.cleaned_data.get('email'))
            return redirect('login')
    context = {'form': form}
    return render(request, "register.html", context)

duration = 0


def home(request):
    if request.user.is_authenticated:
        emp = request.user
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        t1 = datetime.strptime(emp.intime, "%H:%M:%S")
        t2 = datetime.strptime(current_time, "%H:%M:%S")
        duration = t2 - t1
        print("duration in while loop: ",duration)
        time.sleep(1)
        context = {
            "emp": emp,
            "duration": duration,
        }
    else:
        context={}
    return render(request, "home.html", context)
