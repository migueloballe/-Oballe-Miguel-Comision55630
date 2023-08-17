from django import forms
from .models import *

class Cliente_Nuevo(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    direccion = forms.CharField(max_length=200,required=True)
    telefono = forms.IntegerField(required=True)
    correo = forms.CharField(max_length=200,required=False)
    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), required=True)
    fecha = forms.DateTimeField(input_formats=['%d/%m/%Y'], required=True)
    contratacion = forms.CharField(max_length=200,required=True)
    def __str__(self):
        return f"{self.nombre}"
    