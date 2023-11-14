from django.forms import ModelForm
from .models import Tarea

class TareaFormulario(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        exclude = ('fecha',)