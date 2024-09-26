from django.db import models
from pacientes.models import Paciente

# Modelo para el historial de vacunación de un paciente
class HistorialVacunacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Relación con el modelo Paciente
    fecha_vacunacion = models.DateField()  # Fecha de la vacunación
    nombre_vacuna = models.CharField(max_length=100)  # Nombre de la vacuna administrada
    dosis_administrada = models.CharField(max_length=50)  # Dosis administrada

    def __str__(self):
        return f"{self.paciente.nombre} - {self.nombre_vacuna} - {self.fecha_vacunacion}"
