# Generated by Django 4.2.1 on 2023-05-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_employee_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='empid',
            field=models.CharField(max_length=20, null=True, verbose_name='Employee ID'),
        ),
    ]
