from django.urls import path, include
from . import views

app_name = "clinica_APP"

urlpatterns = [
    path('', views.index, name="index"),
    # path("agregar", views.agregar, name=“agregar")
    path('secretaria', views.secretaria, name="secretaria"),
]
