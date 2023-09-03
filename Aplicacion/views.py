from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicio
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth   import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


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

def Nuevo_enfermero(request):
    if request.method == "POST":
        print("Datos recibidos:", request.POST)
        miForm = Enfermero_Nuevo(request.POST)
        if miForm.is_valid():
            print("Formulario válido")
            nombre_form = miForm.cleaned_data.get('nombre')
            direccion_form = miForm.cleaned_data.get('direccion')
            telefono_form = miForm.cleaned_data.get('telefono')
            correo_form = miForm.cleaned_data.get('correo')
            matricula_form = miForm.cleaned_data.get('matricula')
            especialidad_form=miForm.cleaned_data.get('especialidad')

            Nuevo_enferm = Enfermero(nombre=nombre_form,
                                direccion=direccion_form,
                                telefono=telefono_form,
                                correo=correo_form,
                                matricula=matricula_form,
                                especialidad=especialidad_form)
            Nuevo_enferm.save()
            return render(request, "Aplicacion/home.html")

        else:
            print("Formulario no válido", miForm.errors)
    else:
        
        miForm = Enfermero_Nuevo()

    return render(request, "Aplicacion/enfermero.html", {"form": miForm })

def registro(request):
    if request.method == "POST":
        miForm = RegistroCoordinadorForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "Aplicacion/home.html")
    else:
        miForm =  RegistroCoordinadorForm()      
    return render(request, "Aplicacion/registro.html", {"form":miForm}) 


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "Aplicacion/home.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "Aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "Aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "Aplicacion/login.html", {"form":miForm}) 

@login_required
def editarPerfilYAvatar(request):
    usuario = request.user
    u = User.objects.get(username=request.user)
    avatarViejo = Avatar.objects.filter(user=u)

    if request.method == "POST":
        form = UserEditForm(request.POST)
        avatar_form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            # Editar perfil
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            
            # Borrar el avatar viejo
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            # Guardar el nuevo avatar
            avatar = Avatar(user=u, imagen=avatar_form.cleaned_data['avatar'])
            avatar.save()

            return render(request,"Aplicacion/home.html")
        else:
            return render(request, "Aplicacion/editarPerfil.html", {'form': form, 'avatar_form': avatar_form, 'usuario': usuario.username})

    else:
        form = UserEditForm(instance=usuario)
        avatar_form = AvatarFormulario()

    return render(request, "Aplicacion/editarPerfil.html", {'form': form, 'avatar_form': avatar_form, 'usuario': usuario.username})


class ContratoListView(LoginRequiredMixin,ListView):
    model = Contrato
    template_name = 'Aplicacion/contrato_list.html'

class ContratoDetailView(LoginRequiredMixin,DetailView):
    model = Contrato
    template_name = 'Aplicacion/contrato_detail.html'

class ContratoCreateView(LoginRequiredMixin,CreateView):
    model = Contrato
    template_name = 'Aplicacion/contrato_form.html'
    fields = ['paciente', 'servicio', 'especialista', 'fecha', 'condiciones']
    success_url = reverse_lazy('contrato_list')

class ContratoUpdateView(LoginRequiredMixin,UpdateView):
    model = Contrato
    template_name = 'Aplicacion/contrato_form.html'
    success_url = reverse_lazy('contrato_list')
    fields = ['paciente', 'servicio', 'especialista', 'fecha', 'condiciones']

class ContratoDeleteView(LoginRequiredMixin,DeleteView):
    model = Contrato
    template_name = 'Aplicacion/contrato_confirm_delete.html'
    success_url = reverse_lazy('contrato_list')


class ClienteListView(LoginRequiredMixin,ListView):
    model = Persona
    template_name = 'Aplicacion/persona_list.html'

class ClienteDetailView(LoginRequiredMixin,DetailView):
    model = Persona
    template_name = 'Aplicacion/persona_detail.html'
    success_url = reverse_lazy('persona_list')

class ClienteCreateView(LoginRequiredMixin,CreateView):
    model = Persona
    template_name = 'Aplicacion/persona_form.html'
    fields = ['nombre', 'direccion', 'telefono', 'correo']

class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Persona
    template_name = 'Aplicacion/persona_form.html'
    success_url = reverse_lazy('persona_list')
    fields = ['nombre', 'direccion', 'telefono', 'correo']

class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Persona
    template_name = 'Aplicacion/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')

#####

class EnfermeroListView(LoginRequiredMixin,ListView):
    model = Enfermero
    template_name = 'Aplicacion/enfermero_list.html'

class EnfermeroDetailView(LoginRequiredMixin,DetailView):
    model = Enfermero
    template_name = 'Aplicacion/enfermero_detail.html'


class EnfermeroCreateView(LoginRequiredMixin,CreateView):
    model = Enfermero
    template_name = 'Aplicacion/enfermero_form.html'
    fields = ['nombre', 'direccion', 'telefono', 'correo']
    success_url = reverse_lazy('enfermero_list')

class EnfermeroUpdateView(LoginRequiredMixin,UpdateView):
    model = Enfermero
    template_name = 'Aplicacion/enfermero_form.html'
    success_url = reverse_lazy('enfermero_list')
    fields = ['nombre', 'direccion', 'telefono', 'correo']

class EnfermeroDeleteView(LoginRequiredMixin,DeleteView):
    model = Enfermero
    template_name = 'Aplicacion/enfermero_confirm_delete.html'
    success_url = reverse_lazy('enfermero_list')

##

class ServicioListView(LoginRequiredMixin,ListView):
    model = Servicio
    template_name = 'Aplicacion/servicio_list.html'

class ServicioDetailView(LoginRequiredMixin,DetailView):
    model = Servicio
    template_name = 'Aplicacion/servicio_detail.html'

class ServicioCreateView(LoginRequiredMixin,CreateView):
    model = Servicio
    template_name = 'Aplicacion/servicio_form.html'
    fields = ['nombre', 'descripcion', 'costo', 'duracion','otros_detalles']
    success_url = reverse_lazy('servicio_list')

class ServicioUpdateView(LoginRequiredMixin,UpdateView):
    model = Servicio
    template_name = 'Aplicacion/servicio_form.html'
    success_url = reverse_lazy('servicio_list')
    fields = ['nombre', 'descripcion', 'costo', 'duracion','otros_detalles']


class ServicioDeleteView(LoginRequiredMixin,DeleteView):
    model = Servicio
    template_name = 'Aplicacion/servicio_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')