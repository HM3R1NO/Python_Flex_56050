from django.shortcuts import render
from .forms import TareaFormulario
from .models import Tarea
from django.http import HttpResponse

def ver(request):
    tareas = Tarea.objects.all()
    return render(request, 'layouts/tareas/tareas.html', {'tareas': tareas})

def crear(request):
    formulario = TareaFormulario()
    return render(request, 'layouts/tareas/crear-tareas.html', {'formulario': formulario})

def guardar(request):
    if(request.method == 'POST'):
        formulario = TareaFormulario(request.POST)
        if formulario.is_valid:
            formulario.save()
            
            tareas = Tarea.objects.all()
            return render(request, 'layouts/tareas/tareas.html', {'tareas': tareas, 'formulario': formulario})
    else:
        return render(request, 'layouts/tareas/crear-tarea.html', {'formulario': formulario})

def actualizar(request, id):
    tarea = Tarea.objects.get(id=id)
    if(request.method == 'GET'):
        formulario = TareaFormulario(instance = tarea)
        return render(request, 'layouts/tareas/actualizar-tareas.html', {'formulario': formulario, 'id': id})

    if(request.method == 'POST'):
        formulario = TareaFormulario(request.POST, instance = tarea)
        if formulario.is_valid():
            tarea.save()

        tareas = Tarea.objects.all()
        return render(request, 'layouts/tareas/tareas.html', {'tareas': tareas})

def eliminar(request, id):
    if(request.method == 'GET'):
        tarea = Tarea.objects.get(id=id)
        tarea.delete()

        tareas = Tarea.objects.all()
        return render(request, 'layouts/tareas/tareas.html', {'tareas': tareas})

def detalles(request, id):
    if(request.method == 'GET'):
        tarea = Tarea.objects.get(id=id)
        return render(request, 'layouts/tareas/detalles-tareas.html', {'tarea': tarea})