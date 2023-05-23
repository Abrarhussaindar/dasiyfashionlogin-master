
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateEmployee(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'middle_name', 'last_name','username', 'empid','phone_number', 'email','login_counter','logout_counter', 'designation', 'password1', 'password2')