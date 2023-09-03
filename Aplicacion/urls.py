from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    path('servicios/', servicios, name="servicios" ),
    path('contratacion/', contratacion, name="contratacion" ),
    path('contacto/', contacto, name="contacto" ),
    path('registro/', registro, name="registro" ),
    path('enfermero/', Nuevo_enfermero, name="nuevo_enfermero"),
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="Aplicacion/logout.html"), name="logout" ),
    path('editar_perfil/', editarPerfilYAvatar, name="editar_perfil" ),

    path('contratos/', ContratoListView.as_view(), name='contrato_list'),
    path('contrato/<int:pk>/', ContratoDetailView.as_view(), name='contrato_detail'),
    path('contrato/new/', ContratoCreateView.as_view(), name='contrato_new'),
    path('contrato/<int:pk>/edit/', ContratoUpdateView.as_view(), name='contrato_edit'),
    path('contrato/<int:pk>/delete/', ContratoDeleteView.as_view(), name='contrato_delete'), 

    path('persona/', ClienteListView.as_view(), name='persona_list'),
    path('persona/<int:pk>/', ClienteDetailView.as_view(), name='persona_detail'),
    path('persona/new/', ClienteCreateView.as_view(), name='persona_new'),
    path('persona/<int:pk>/edit/', ClienteUpdateView.as_view(), name='persona_edit'),
    path('persona/<int:pk>/delete/', ClienteDeleteView.as_view(), name='persona_delete'),

    path('enfermeroview/', EnfermeroListView.as_view(), name='enfermero_list'),
    path('enfermero/<int:pk>/', EnfermeroDetailView.as_view(), name='enfermero_detail'),
    path('enfermero/new/', EnfermeroCreateView.as_view(), name='enfermero_new'),
    path('enfermero/<int:pk>/edit/', EnfermeroUpdateView.as_view(), name='enfermero_edit'),
    path('enfermero/<int:pk>/delete/', EnfermeroDeleteView.as_view(), name='enfermero_delete'),

    path('enfermeroview/', EnfermeroListView.as_view(), name='enfermero_list'),
    path('enfermero/<int:pk>/', EnfermeroDetailView.as_view(), name='enfermero_detail'),
    path('enfermero/new/', EnfermeroCreateView.as_view(), name='enfermero_new'),
    path('enfermero/<int:pk>/edit/', EnfermeroUpdateView.as_view(), name='enfermero_edit'),
    path('enfermero/<int:pk>/delete/', EnfermeroDeleteView.as_view(), name='enfermero_delete'),

    path('servicioview/', ServicioListView.as_view(), name='servicio_list'),
    path('servicio/<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
    path('servicio/new/', ServicioCreateView.as_view(), name='servicio_new'),
    path('servicio/<int:pk>/edit/', ServicioUpdateView.as_view(), name='servicio_edit'),
    path('servicio/<int:pk>/delete/', ServicioDeleteView.as_view(), name='servicio_delete'),

    ]


