from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('servicios/', servicios, name="servicios" ),
    path('contratacion/', contratacion, name="contratacion" ),
    path('contacto/', contacto, name="contacto" ),
]

