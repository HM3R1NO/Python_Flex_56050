from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor
from django.http import HttpResponse
from AppCoder.forms import EstudianteForm, ProfesorForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from App12.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def profesor12(request):
    if request.method == "POST":
            miFormulario = ProfesorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                profesor = Profesor(nombre=informacion["nombre"], apellidade=informacion["apellidade"], email=informacion["email"], edad=informacion["edad"])
                profesor.save()
                messages.success(request, 'El profesor ha sido creado con éxito.')
                return render(request, "AppCoder/index.html")
    else:
            miFormulario = ProfesorForm()
    return render(request, "App12/profesores12.html", {"miFormulario": miFormulario})

def leerProfesores12(request):
    profesores = Profesor.objects.all() #trae todos los profesores
    contexto= {"profesores":profesores}
    return render(request, "App12/leerProfesores12.html",contexto)

def eliminarProfesor12(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
    contexto = {"profesores": profesores}
    return render(request, "App12/leerProfesores12.html", contexto)

def editarProfesor12(request, profesor_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProfesorForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellidade = informacion['apellidade']
            profesor.email = informacion['email']
            profesor.edad = informacion['edad']

            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/index.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorForm(initial={'nombre': profesor.nombre, 'apellidade': profesor.apellidade,'email': profesor.email, 'edad': profesor.edad})

    # Voy al html que me permite editar
    return render(request, "App12/editarProfesor12.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})


#========================================================
class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "App12/curso_lista.html"


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "App12/curso_detalle.html"


class CursoCreateView(CreateView):
    model = Curso
    template_name = "App12/curso_crear.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada','imagen']


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "App12/curso_editar.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada', 'imagen']

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "App12/curso_borrar.html"
    success_url = reverse_lazy('ListaCursos')
    
    
