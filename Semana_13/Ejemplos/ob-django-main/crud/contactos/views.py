from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacto
from .forms import ContactoFormulario


def todos(request):
    # if(request.GET['search']):
    #     recuperar_todos = Contacto.objects.filter(nombre__contains = request.GET.get('search', ''))
    # else:
    recuperar_todos = Contacto.objects.all()
    return render(request, 'layouts/contactos/contactos.html', {'recuperar_todos': recuperar_todos})

def ver(request, nombre):
    formulario = Contacto.objects.get(nombre=nombre)
    return render(request, 'layouts/contactos/ver-contacto.html', {'formulario': formulario})

def crear(request):
    formulario = ContactoFormulario()
    return render(request, 'layouts/contactos/crear-contacto.html', {'formulario': formulario})

def guardar(request):
    if(request.method == "POST"):
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()

            recuperar_todos = Contacto.objects.all()
            return render(request, 'layouts/contactos/contactos.html', {'formulario': formulario, 'recuperar_todos': recuperar_todos})
    else:
        return render(request, 'layouts/contactos/crear-contacto.html', {'formulario': formulario})


def actualizar(request, nombre):
    contacto = Contacto.objects.get(nombre=nombre)
    if(request.method == 'GET'):
        formulario = ContactoFormulario(instance = contacto)
        return render(request, 'layouts/contactos/actualizar-contacto.html', {'formulario': formulario, 'nombre': nombre})

    if(request.method == 'POST'):
        formulario = ContactoFormulario(request.POST, instance=contacto)
        if formulario.is_valid():
            formulario.save()

            recuperar_todos = Contacto.objects.all()
        return render(request, 'layouts/contactos/contactos.html', {'formulario': formulario, 'nombre': nombre, 'recuperar_todos': recuperar_todos})

def eliminar(request, nombre):
    if(request.method == 'GET'):
        contacto = Contacto.objects.get(nombre = nombre)
        contacto.delete()

        recuperar_todos = Contacto.objects.all()
        return render(request, 'layouts/contactos/contactos.html', {'recuperar_todos': recuperar_todos})
    
    