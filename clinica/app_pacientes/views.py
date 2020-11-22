from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import datetime

# Create your views here.


def index(request):
    return render(request, "secretaria/verPaciente.html")


# antiguo view
def agregar(request):
    return render(request, "secretaria/agregarPaciente.html", {
        "form": Form_datospersonales()
    }
    )


'''
def agregar(request):
    if request.method == "POST":
        form = Form_datospersonales(request.POST)
    if form.is_valid():
        datos = form.cleaned_data["app_paciente"]
        "app_pacientes": request.session["app_pacientes"]

# Agregar la nueva tarea a nuestra lista de tareas tareas.append(tarea)
# Redireccionar al usuario a la lista de tareas return HttpResponseRedirect(reverse("tareas:index"))
    else:  # Si el formulario es invalido, volver a renderizar la pagina con la informacion existente.
        return render(request, "app_pacientes/agregar.html", {
            "form": form
        })

    return render(request, "app_pacientes/agregar.html", {
        "form": Form_datospersonales()
    })
'''


def home(request):
    return render(request, "home.html")


class Form_datospersonales(forms.Form):
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    dni = forms.IntegerField(label="DNI")
    telefono = forms.IntegerField(label="Telefono")
    fecha_nac = forms.DateField(initial=datetime.date.today)
