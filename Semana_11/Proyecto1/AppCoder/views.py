from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor
from django.http import HttpResponse
from AppCoder.forms import EstudianteForm, ProfesorForm

# Create your views here.
def curso(self):
    curso = Curso(nombre="Python", camada=55555)
    curso.save()
    documentoDeTexto = f"----->Curso {curso.nombre} Camada {curso.camada}" 
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return HttpResponse('<h1>vista profesores</h1>')

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return HttpResponse('vista entregables')

def cursoForm(request):
    # Aca pregunta que metodo es post envio get traigo
    # if request.method == 'POST':
    #     pepe = Curso(request.POST['nombre'],request.POST['camada'])#<- traigo del template los datos de los input
    #     pepe.save()
    #     return render(request, "AppCoder/index.html")    
    # return render(request, "AppCoder/cursoForm.html")


    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        return render(request, "AppCoder/index.html")
    return render(request, "AppCoder/cursoForm.html")

def estudianteForm(request):
    if request.method == 'POST':
        miFormulario = EstudianteForm(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Estudiante(nombre = info['nombre'], apellidade = info['apellidade'], email = info['email'])
            info.save()
            return render(request, 'AppCoder/index.html')
    else:
        miFormulario = EstudianteForm()
    return render(request, "AppCoder/estudianteForm.html",{'miFormulario':miFormulario})

def profesorForm(request):
    if request.method == 'POST':
        miFormulario = ProfesorForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            data = Profesor(nombre = data['nombre'], apellidade = data['apellidade'], email = data['email'], edad = data['edad'])
            data.save()
            return render(request, 'AppCoder/index.html')
    else:
        miFormulario = ProfesorForm()
    return render(request, 'AppCoder/profesorForm.html', {"miFormulario":miFormulario})

