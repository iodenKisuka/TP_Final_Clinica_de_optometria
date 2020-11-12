from django.urls import path, include
from . import views

app_name = "app_pedidos"

urlpatterns = [
    path('', views.index, name="index"),
    path('/pedido', views.imprimir, name="index"),
    path('/nuevo', views.nuevo, name="nuevo"),
]
