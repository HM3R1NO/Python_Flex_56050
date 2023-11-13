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
    
    
    #login
    path('login/', login_view, name="Login"),
    path('register/', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', editarPerfil, name="editarPerfil"), 
    path('cambiarContrasenia', CambiarContrasenia.as_view(), name="CambiarContrasenia"),
]