from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
