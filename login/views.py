from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import time
import threading

import time

# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         time_sec += 1

#     print("stop")

# countdown(1)


# import datetime
  
# # # creating an instance of 
# # # datetime.time
# # # time(hour = 0, minute = 0, second = 0)
# d = datetime.time(0, 0, 0)
  
# # creating an instance of 
# # GeeksModel
# geek_object = GeeksModel.objects.create(geeks_field = d)
# geek_object.save()

# Create your views here.
def user_login(request):
    print("current time", time.strftime("%H:%M:%S", time.localtime()))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        print(username, password)
        employee = authenticate(request, username=username, password=password)
        print(employee)
        # employe_counter = Employee.objects.filter(empid=employee.empid)
        employe_counter = employee.counter
        print("login counts: ",employe_counter)
        if employee == None:
            print("yes")
        print("yes it is: ", employee.is_authenticated)
        if employee is not None:
            print("employee is not none")
            # countdown(1)
            employee.counter += 1
            login(request, employee)
            employe_counter = employee.counter
            employee.save()
            print("login counts: ",employe_counter)
            return redirect('home')
            
    context = {}
    return render(request, "login.html", context)

def home(request):
    # employee.counter += 1
    return render(request, "home.html", {})


# if __name__ =="__main__":
#     # creating thread
#     t1 = threading.Thread(target=user_login)
#     t2 = threading.Thread(target=countdown)
 
#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()

#     t1.join()
#     # wait until thread 2 is completely executed
#     t2.join()
 