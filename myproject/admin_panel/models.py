from django.db import models

# Modelo para las unidades de salud
class UnidadSalud(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre de la unidad de salud
    direccion = models.CharField(max_length=255)  # Dirección de la unidad de salud
    telefono = models.CharField(max_length=20)  # Teléfono de contacto
    servicios_disponibles = models.TextField()  # Servicios disponibles en la unidad

    def __str__(self):
        return self.nombre  # Devuelve el nombre de la unidad de salud
