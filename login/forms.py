
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateEmployee(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('name','username', 'empid','designation', 'department','phone_number', 'email','login_counter','logout_counter',  'password1', 'password2')


# class ManagmentTeamForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ('name','username', 'empid','designation', 'department','phone_number', 'email','login_counter','logout_counter',  'password1', 'password2')

# class OperationsTeamForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ('name','username', 'empid','designation', 'department','phone_number', 'email','login_counter','logout_counter',  'password1', 'password2')

# class MarketingTeamForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ('name','username', 'empid','designation', 'department','phone_number', 'email','login_counter','logout_counter',  'password1', 'password2')

# class SalesTeamForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ('name','username', 'empid','designation', 'department','phone_number', 'email','login_counter','logout_counter',  'password1', 'password2')

# class ITTeamForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ('name','username', 'empid','designation', 'department','phone_number', 'email','login_counter','logout_counter',  'password1', 'password2')
