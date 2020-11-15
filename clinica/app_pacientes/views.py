from django.shortcuts import render
from django import forms

# Create your views here.
def index(request):
    return render(request, "app_pacientes/indexPaciente.html")

def agregar(request):
    return render(request, "app_pacientes/agregarPaciente.html")


def home(request):
    return render(request, "home.html")




class datospersonales(forms.Form):
    nombre = forms.CharField(label="nombre")
    apellido = forms.CharField(label="apellido")
    dni = forms.IntegerField(label="dni")
    telefono = forms.IntegerField(label="telefono")
    fecha_nac = forms.DateField()
