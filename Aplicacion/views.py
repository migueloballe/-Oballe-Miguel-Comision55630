from django.shortcuts import render
from django.http import HttpResponse

from .models import Servicio
from .models import *
from .forms import *
#from .forms import CursoForm

# Create your views here.

def home(request):
    return render(request, "Aplicacion/home.html")


def contacto(request):
    return render(request, "Aplicacion/contacto.html")

def servicios(request):
    query = request.GET.get('buscar', '')
    servicios = Servicio.objects.all()
    
    if query:
        servicios = servicios.filter(nombre__icontains=query)
    
    contexto = {'servicios': servicios, 'titulo': 'Nuestros servicios'}
    return render(request, "Aplicacion/servicios.html", contexto)

def contratacion(request):
    if request.method == "POST":
        print("Datos recibidos:", request.POST)
        miForm = Cliente_Nuevo(request.POST)
        if miForm.is_valid():
            print("Formulario válido")
            nombre_form = miForm.cleaned_data.get('nombre')
            direccion_form = miForm.cleaned_data.get('direccion')
            telefono_form = miForm.cleaned_data.get('telefono')
            correo_form = miForm.cleaned_data.get('correo')
            servicioelegido = miForm.cleaned_data.get('servicio')
            fechaelegida=miForm.cleaned_data.get('fecha')
            condicioneselegidas=miForm.cleaned_data.get('contratacion')

            Nuevo_cli = Persona(nombre=nombre_form,
                                direccion=direccion_form,
                                telefono=telefono_form,
                                correo=correo_form)
            Nuevo_cli.save()
            Nuevo_contrato= Contrato(paciente=Nuevo_cli,
                                     servicio=servicioelegido,
                                     fecha=fechaelegida,
                                     condiciones=condicioneselegidas)
            Nuevo_contrato.save()
            return render(request, "Aplicacion/home.html")
        else:
            print("Formulario no válido", miForm.errors)
    else:
        
        miForm = Cliente_Nuevo()
    
    return render(request, "Aplicacion/contratacion.html", {"form": miForm })

