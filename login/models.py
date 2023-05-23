from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import time



class MyUserManager(BaseUserManager):
    def create_user(self, username, email,intime,department, duration_time,out_time,logout_counter, login_counter, empid, name, designation, phone_number, password=None):

        user=self.model(
            email=self.normalize_email(email),
            username = username,
            login_counter=login_counter,
            logout_counter=logout_counter,
            name = name,
            intime=intime,
            out_time=out_time,
            duration_time=duration_time,
            phone_number = phone_number,
            designation = designation,
            department=department,
            empid = empid,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,username, login_counter,department,duration_time,logout_counter,intime,out_time, email, empid, name, designation, phone_number, password=None):
        user=self.create_user(
            email=email,
            username = username,
            name = name,
            # middle_name = middle_name,
            # last_name = last_name,
            designation = designation,
            department=department,
            empid = empid,
            login_counter=login_counter,
            logout_counter=logout_counter,
            intime=intime,
            out_time=out_time,
            duration_time=duration_time,
            phone_number = phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

login_times = []
logout_times = []

import math
 
# Defining a positive infinite integer
positive_infinity = math.inf


from django.db import models
from typing import Iterable

class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

class ListModel(models.Model):
    test_list = ListField()

class Employee(AbstractBaseUser):
    name = models.CharField(verbose_name='Name', max_length=200, null=True)
    # middle_name = models.CharField(verbose_name='Middle Name', max_length=200, null=True)
    # last_name = models.CharField(verbose_name='Last Name', max_length=200, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=10, null=True)
    username = models.CharField(verbose_name='Username', max_length=20, null=True, unique=True)
    empid = models.CharField(verbose_name='Employee ID', max_length=20, null=True)
    designation = models.CharField(verbose_name='Designation', max_length=50, null=True)
    department = models.CharField(verbose_name='Depertment', max_length=50, null=True)

    login_counter = models.IntegerField(verbose_name="No. Of LogIn\'s", default=0, null=True)
    logout_counter = models.IntegerField(verbose_name="No. Of Logout\'s", default=0, null=True)

    intime = models.CharField(verbose_name='Current Login Time',max_length=200, null=True)
    out_time = models.CharField(verbose_name='Previous LogOut Time',max_length=200, null=True)
    duration_time = models.CharField(verbose_name='Last Login Duration',max_length=200, null=True)

    login_list = ListField(verbose_name="Login List", null=True)
    logout_list = ListField(verbose_name="Logout List", null=True)
    duration_list = ListField(verbose_name="Login Duration List", null=True)


    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone_number', 'counter', 'email', 'empid', 'designation', 'department']

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True