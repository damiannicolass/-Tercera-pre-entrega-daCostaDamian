# Generated by Django 5.0.6 on 2024-07-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguros', '0002_rename_asegurados_asegurado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siniestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sinietro', models.CharField(max_length=30)),
                ('asegurado', models.CharField(max_length=30)),
                ('informacion', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=5000)),
            ],
        ),
    ]
