from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
class Enfermero_Nuevo(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    direccion = forms.CharField(max_length=200,required=True)
    telefono = forms.IntegerField(required=True)
    correo = forms.CharField(max_length=200,required=False)
    especialidad = forms.CharField(max_length=50)
    matricula = forms.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre}"
    
class RegistroCoordinadorForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Coordinador")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)  

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField(required=False)