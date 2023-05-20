from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import time



class MyUserManager(BaseUserManager):
    def create_user(self, username, email,intime, out_time, counter, empid, first_name, middle_name, last_name, designation, phone_number, password=None):

        user=self.model(
            email=self.normalize_email(email),
            username = username,
            counter=counter,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            intime=intime,
            out_time=out_time,
            phone_number = phone_number,
            designation = designation,
            empid = empid,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,username, counter,intime,out_time, email, empid, first_name, middle_name, last_name, designation, phone_number, password=None):
        user=self.create_user(
            email=email,
            username = username,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            designation = designation,
            empid = empid,
            counter=counter,
            intime=intime,
            out_time=out_time,
            phone_number = phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

login_times = []

class Employee(AbstractBaseUser):
    first_name = models.CharField(verbose_name='First Name', max_length=200, null=True)
    middle_name = models.CharField(verbose_name='Middle Name', max_length=200, null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=200, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=10, null=True)
    username = models.CharField(verbose_name='Username', max_length=20, null=True, unique=True)
    empid = models.CharField(verbose_name='Employee ID', max_length=20, null=True)
    designation = models.CharField(verbose_name='Designation', max_length=20, null=True)

    counter = models.IntegerField(verbose_name="Logged In", default=0, null=True)

    # login_details = models.QuerySet(verbose_name="login_details", )
    intime = models.TimeField(verbose_name='Login Time',auto_now=False, null=True)
    out_time = models.TimeField(verbose_name='LogOut Time',auto_now=False, null=True)


    # course = models.CharField(verbose_name='Course', max_length=200, null=True)
    # admitted_through = models.CharField(verbose_name='Admitted Through', max_length=200, null=True)
    # applied_year = models.CharField(verbose_name='Applied Year', max_length=20, null=True)
    # address = models.CharField(verbose_name='address', max_length=500, null=True)
    # city = models.CharField(verbose_name='city', max_length=200, null=True)
    # state = models.CharField(verbose_name='state', max_length=200, null=True)
    # country = models.CharField(verbose_name='country', max_length=100, null=True)
    # alternate_address = models.CharField(verbose_name='alternate_address', max_length=500, null=True)
    # house_number = models.CharField(verbose_name='house_number', max_length=5, null=True)
    # pincode = models.CharField(verbose_name='pincode', max_length=10, null=True)

    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','middle_name', 'last_name', 'phone_number', 'counter', 'email', 'empid', 'designation']

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True