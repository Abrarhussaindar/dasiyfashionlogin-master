# Generated by Django 4.2.1 on 2023-05-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_alter_employee_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='counter',
            field=models.IntegerField(default=0, null=True, verbose_name='Logged In'),
        ),
    ]