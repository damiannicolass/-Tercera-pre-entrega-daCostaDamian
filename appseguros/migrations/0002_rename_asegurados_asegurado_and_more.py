# Generated by Django 5.0.6 on 2024-07-24 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appseguros', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Asegurados',
            new_name='Asegurado',
        ),
        migrations.RenameModel(
            old_name='Empleados',
            new_name='Empleado',
        ),
        migrations.RenameModel(
            old_name='Vehiculos',
            new_name='Vehiculo',
        ),
    ]
