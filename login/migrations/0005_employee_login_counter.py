# Generated by Django 4.2.1 on 2023-05-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_employee_empid'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='login_counter',
            field=models.TimeField(null=True, verbose_name='counter'),
        ),
    ]