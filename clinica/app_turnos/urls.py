from django.urls import path, include
from . import views

app_name ="app_turnos"

urlpatterns = [
    path('', views.index, name="index"),
]
