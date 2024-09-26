from django.db import models
from pacientes.models import Paciente

# Modelo para gestionar citas médicas
class CitaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Relación con el modelo Paciente
    fecha_hora = models.DateTimeField()  # Fecha y hora de la cita
    motivo = models.TextField()  # Motivo de la cita

    def __str__(self):
        return f"Cita de {self.paciente.nombre} el {self.fecha_hora}"
