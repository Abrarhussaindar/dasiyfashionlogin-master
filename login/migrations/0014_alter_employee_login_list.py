# Generated by Django 4.2.1 on 2023-05-20 10:40

from django.db import migrations
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_listmodel_employee_login_list_employee_logout_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='login_list',
            field=login.models.ListField(null=True, token=',', verbose_name='Login List'),
        ),
    ]