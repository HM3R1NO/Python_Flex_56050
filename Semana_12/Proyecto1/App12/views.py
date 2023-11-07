from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor
from django.http import HttpResponse
from AppCoder.forms import EstudianteForm, ProfesorForm

# Create your views here.
def profesor12(request):
    if request.method == "POST":
            miFormulario = ProfesorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                profesor = Profesor(nombre=informacion["nombre"], apellidade=informacion["apellidade"], email=informacion["email"], edad=informacion["edad"])
                profesor.save()
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
