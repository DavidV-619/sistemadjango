from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tipo')

def __str__(self):
    return self.name

class Meta:
    verbose_name='Tipo'
    verbose_name_plural='Tipos'
    ordering = ['id']


class Empleado(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=100, verbose_name='Nombres')
    puesto = models.CharField(max_length=100, verbose_name='Puesto')
    clave = models.CharField(max_length=10, unique=True, verbose_name='Clave' )
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro' )
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='foto/$Y/%m/%d', null=True, blank=True)
    cv = models.FileField(upload_to='info/$Y/%m/%d', null=True, blank=True)


def __str__(self):
        return self.names
    


class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordening = ['id']
