from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name="home"),
    path('cursos/', cursos, name="curioso"),
    path('profesores/', profesores, name="profe"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name='entregables'),
    # path('curso/',curso,name='curso'),
    
    #Url de formularios 
    path('cursoForm/',cursoForm, name='cursoForm'),
    path('estudianteForm/',estudianteForm, name='estudianteForm'),
    path('profesorForm/', profesorForm, name='profesorForm'),
]