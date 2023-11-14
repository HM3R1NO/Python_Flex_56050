from django import forms

class EstudianteForm(forms.Form):
    nombre = forms.CharField()
    apellidade = forms.CharField()
    email = forms.EmailField()
    
    
class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellidade = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    

    
    
    