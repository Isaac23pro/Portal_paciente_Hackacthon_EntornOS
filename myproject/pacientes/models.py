from django.db import models
from django.contrib.auth.models import User

# Modelo para representar a un paciente
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo User
    nombre = models.CharField(max_length=100)  # Nombre del paciente
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento
    direccion = models.CharField(max_length=255)  # Dirección del paciente
    telefono = models.CharField(max_length=20)  # Teléfono del paciente

    def __str__(self):
        return self.nombre  # Devuelve el nombre del paciente

# Modelo para almacenar el historial médico del paciente
class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Relación con el modelo Paciente
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha del registro del historial
    motivo_ingreso = models.TextField()  # Motivo de ingreso del paciente
    diagnostico = models.TextField()  # Diagnóstico realizado
    procedimiento_realizado = models.TextField()  # Procedimientos realizados
    resultados_examenes = models.TextField()  # Resultados de los exámenes
    imagenes_diagnosticas = models.TextField()  # Referencia a imágenes diagnósticas

    def __str__(self):
        return f"Historial de {self.paciente.nombre} - {self.fecha}"
