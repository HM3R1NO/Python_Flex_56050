from django.forms import ModelForm 
from .models import Contacto

class ContactoFormulario(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        # fields = ['nombre','apellidos','movil','email']