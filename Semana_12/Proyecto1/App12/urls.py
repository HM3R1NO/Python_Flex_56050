from django.urls import path
from App12.views import *

urlpatterns = [
    path('profesores12/', profesor12, name='profesor12'),
    path('leerProfesores12', leerProfesores12, name = "leerProfesores12"),
    path('eliminarProfesor12/<profesor_nombre>/', eliminarProfesor12, name="eliminarProfesor12"),
]