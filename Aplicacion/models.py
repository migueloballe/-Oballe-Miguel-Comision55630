from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo = models.EmailField(blank=True, null=True)
    def __str__(self):
        return f"{self.nombre}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.DurationField()
    otros_detalles = models.TextField()
    def __str__(self):
        return f"{self.nombre}"

class Enfermero(Persona):
    especialidad = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

class Contrato(models.Model):
    paciente = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='contratos')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    especialista = models.ForeignKey(Enfermero, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField()
    condiciones = models.TextField()
    def __str__(self):
        return f"{self.servicio} {self.fecha} {self.paciente}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} {self.imagen}"