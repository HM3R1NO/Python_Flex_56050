from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_cursos', null=True, blank = True)
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellidade = models.CharField(max_length=30)
    email = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidade = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellidade} - E-Mail {self.email} - Edad {self.edad}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    descripcion = models.TextField(null=True)
    link = models.URLField(null=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"

