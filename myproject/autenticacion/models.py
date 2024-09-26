from django.db import models
from django.contrib.auth.models import User

# Modelo para el perfil del usuario que extiende el modelo User de Django
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo User
    # Aquí puedes agregar más campos específicos del perfil si lo necesitas

    def __str__(self):
        return self.user.username  # Devuelve el nombre de usuario

# Modelo para manejar la autenticación de doble factor
class DobleAutenticacion(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)  # Relación con el perfil del usuario
    metodo = models.CharField(max_length=50)  # Método de autenticación, e.g., SMS, email, app
    token = models.CharField(max_length=100)  # Token generado para la autenticación
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación del token

    def __str__(self):
        return f"Autenticación de {self.usuario.user.username} con {self.metodo}"

