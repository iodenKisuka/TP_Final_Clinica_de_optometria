from django.shortcuts import render
from django import forms
# Create your views here.


def index(request):
    return render(request, "indexPedido.html")


pedidos = ["pedido1", "pedido 2"]


def imprimir(request):
    return render(request, "indexPedido.html", {
        "pedidos": pedidos
    })


class MiNuevoFormulario(forms.Form):
    producto = forms.CharField(label="Nuevo Producto")


# Agregando en el contexto del paso al template:


def nuevo(request):
    return render(request, "producto/nuevo.html", {
        "formulario_producto_nuevo": MiNuevoFormulario()
    })
