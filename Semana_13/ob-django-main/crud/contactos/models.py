from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    movil = models.CharField(max_length=9, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre
    