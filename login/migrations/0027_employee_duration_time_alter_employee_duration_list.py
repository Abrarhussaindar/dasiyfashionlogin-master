# Generated by Django 4.2.1 on 2023-05-22 05:05

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_employee_duration_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='duration_time',
            field=models.CharField(max_length=200, null=True, verbose_name='Login Time Duration'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='duration_list',
            field=login.models.ListField(null=True, token=',', verbose_name='Login Duration List'),
        ),
    ]
