from django.db import models
from app_turnos import *

# Create your models here.


class Paciente(models.Model):
    nombrePac = models.CharField(max_length=64)
    apellidoPac = models.CharField(max_length=64)
    dniPac = models.IntegerField()
    telefonoP = models.IntegerField()
    fecha_nacPac = models.DateField()


class HistorialMedico:
   paciente_id = models.ForeignKey(
       Paciente, on_delete=models.CASCADE, related_name="paciente")


