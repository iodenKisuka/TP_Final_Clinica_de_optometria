from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"indexPaciente.html")

def agregar(request):
    return render(request, "agregarPaciente.html")


def home(request):
    return render(request, "home.html")
