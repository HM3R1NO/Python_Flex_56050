from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor, Avatar
from django.http import HttpResponse, HttpResponseNotFound
from AppCoder.forms import EstudianteForm, ProfesorForm
from App12.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


from django.core.files import File


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


#=========================================================
#Login

def login_view(request):

    if request.method == "POST": #click al boton iniciar sesion

        form_inicio = AuthenticationForm(request, data = request.POST)
        
        if form_inicio.is_valid(): #el formulario nos ayuda a validar

            info = form_inicio.cleaned_data #data que se escribio en el formulario de login en modo diccionario 
            usuario = info.get("username")
            contra = info.get("password")

            #acá hacemos la validación
            user = authenticate(username=usuario, password=contra) #existe el usuario (retorna el usuario) ---- no existe usuario (retorna None)

            if user:
                login(request, user)    #iniciar sesion ya que el usuario si existe (credenciales correctas)
                return render(request, "AppCoder/index.html", {"usuario":user})
        
        else:
            return render(request,"AppCoder/index.html", {"mensaje":"DATOS INCORRECTOS"})

    form_inicio = AuthenticationForm() #formulario vacio

    return render(request,"App12/login.html", {"form":form_inicio} )



#=======================================
# Vista de registro
def register(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})
    else:
            form = UserCreationForm()
            #form = UserRegisterForm()
    return render(request,"App12/register.html" ,  {"form":form})


# Vista de editar el perfil
@login_required
@login_required
def editarPerfil(request):
    usuario = request.user

    # Manejar solicitudes para favicon.ico
    if request.path == '/favicon.ico/':
        return HttpResponseNotFound()

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if hasattr(usuario, 'avatar') and usuario.avatar:
                if miFormulario.cleaned_data.get('imagen'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    # Si no se proporciona una imagen, establece una imagen por defecto
                    imagen_por_defecto = 'media/avatares/nonavatar.png'
                    with open(imagen_por_defecto, 'rb') as f:
                        usuario.avatar.imagen.save('imagen_por_defecto.jpg', File(f))
            else:
                # Si el usuario no tiene un avatar, crea uno y guarda la imagen
                avatar = Avatar.objects.create(user=usuario)
                if miFormulario.cleaned_data.get('imagen'):
                    avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    avatar.save()
                else:
                    # Si no se proporciona una imagen, establece una imagen por defecto
                    imagen_por_defecto = 'media/avatares/nonavatar.png'
                    with open(imagen_por_defecto, 'rb') as f:
                        avatar.imagen.save('imagen_por_defecto.jpg', File(f))

            miFormulario.save()
            return render(request, "AppCoder/index.html")
    else:
        # Si el usuario no tiene avatar, crea uno y establece la imagen por defecto en el formulario
        if not hasattr(usuario, 'avatar') or not usuario.avatar:
            avatar = Avatar.objects.create(user=usuario)
            imagen_por_defecto = 'media/avatares/nonavatar.png'
            with open(imagen_por_defecto, 'rb') as f:
                avatar.imagen.save('imagen_por_defecto.jpg', File(f))

        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)

    return render(request, "AppCoder/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppCoder/editar_contrasenia.html'
    success_url = reverse_lazy('editarPerfil')