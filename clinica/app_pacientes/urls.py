from django.urls import path, include
from . import views

app_name = "app_pacientes"

urlpatterns = [
    path('agregar', views.agregar, name="agregar"),
    path('', views.index, name="index"),
    path('/h', views.home, name="home"),
]
