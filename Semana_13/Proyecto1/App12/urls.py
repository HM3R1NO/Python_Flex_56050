from django.urls import path
from App12.views import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


urlpatterns = [
    path('profesores12/', profesor12, name='profesor12'),
    path('leerProfesores12', leerProfesores12, name = "leerProfesores12"),
    path('eliminarProfesor12/<profesor_nombre>/', eliminarProfesor12, name="eliminarProfesor12"),
    path('editarProfesor12/<profesor_nombre>/', editarProfesor12, name="editarProfesor12"),
    
    
    #CBV ==================================================
    path('lista/', CursoListView.as_view(), name = "ListaCursos"),
    path('nuevo/', CursoCreateView.as_view(), name = "NuevoCurso"),
    path('<pk>/', CursoDetailView.as_view(), name = "DetalleCurso"),
    path('<pk>/editar/', CursoUpdateView.as_view(), name = "EditarCurso"),
    path('<pk>/borrar/', CursoDeleteView.as_view(), name = "BorrarCurso"),
]