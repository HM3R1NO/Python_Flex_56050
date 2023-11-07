from datetime import date
from django.db import models
from django.forms import forms

class Tarea(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=True, null=False)
    fecha = models.DateField(default=date.today)
    fecha_entrega = models.DateField(blank=True, null=True)
    prioridad = models.IntegerField(default=3)

    def __str__(self):
        return self.titulo
    