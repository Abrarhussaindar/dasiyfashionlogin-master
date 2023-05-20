
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateStudent(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'middle_name', 'last_name','username', 'empid', 'email','login_counter','logout_counter', 'designation', 'password1', 'password2')