from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    horario = models.CharField(max_length=11)
    puesto = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=500)
    tipo_sangre = models.CharField(max_length=3)
    rfc = models.CharField(max_length=15)
    curp = models.CharField(max_length=18)