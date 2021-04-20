# Generated by Django 3.1.3 on 2021-04-19 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('puesto', models.CharField(max_length=100, verbose_name='Puesto')),
                ('clave', models.CharField(max_length=10, unique=True, verbose_name='Clave')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='foto/$Y/%m/%d')),
                ('cv', models.FileField(blank=True, null=True, upload_to='info/$Y/%m/%d')),
            ],
        ),
    ]