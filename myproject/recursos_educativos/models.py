from django.db import models

# Modelo para los recursos educativos
class RecursoEducativo(models.Model):
    titulo = models.CharField(max_length=200)  # Título del recurso educativo
    contenido = models.TextField()  # Contenido del recurso
    fecha_publicacion = models.DateTimeField(auto_now_add=True)  # Fecha de publicación del recurso

    def __str__(self):
        return self.titulo  # Devuelve el título del recurso

# Modelo para las notificaciones relacionadas a los recursos educativos
class Notificacion(models.Model):
    recurso = models.ForeignKey(RecursoEducativo, on_delete=models.CASCADE)  # Relación con el recurso educativo
    metodo_notificacion = models.CharField(max_length=50)  # Método de notificación, e.g., WhatsApp, email
    mensaje = models.TextField()  # Mensaje de la notificación

    def __str__(self):
        return f"Notificación para {self.recurso.titulo}"
