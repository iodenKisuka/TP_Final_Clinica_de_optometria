from django.db import models
# import paquete.modulo1
# import app_pacientes.models
from app_pacientes.models import Paciente
# Create your models here.


class Medico(models.Model):
    nombreMed = models.CharField(max_length=64)
    apellidoMed = models.CharField(max_length=64)
    dniMed = models.IntegerField()
    telefonoMed = models.IntegerField()
    

class Turno(models.Model):
    fecha_turno = models.DateField()
    paciente_T = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="paciente")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="paciente")


