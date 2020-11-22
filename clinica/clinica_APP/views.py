from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, "index.html")



# def agregar(request):
   # return render(request, "tareas/agregar.html")


def ingresar(request):
    if (request.method == 'POST'):
        username = request.POST.get('menuRol')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(pagina())

    return render(request, 'index.html',
                  {})


def pagina():
    # if(user==)
    #'nombre del name de url'
    # podria ser app:
    print("usuario ")


def secretaria(request):
    return render(request, "secretaria.html")
