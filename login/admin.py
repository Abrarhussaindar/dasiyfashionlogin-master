from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display = ('first_name','middle_name' , 'empid', 'username', 'email', 'designation',  'is_active', 'is_staff', 'is_admin')
    search_fields = ('username', 'email')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('first_name' , 'middle_name' , 'last_name' , 'phone_number', 'empid','designation', 'username', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ('first_name', 'middle_name', 'last_name', 'username', 'email',)

admin.site.register(Employee, MyUserAdmin)