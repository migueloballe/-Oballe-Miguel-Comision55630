from django.db import models

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

class Contrato(models.Model):
    paciente = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='contratos')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    condiciones = models.TextField()
