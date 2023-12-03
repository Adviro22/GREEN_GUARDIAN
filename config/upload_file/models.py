from django.db import models
from datetime import datetime

# Create your models here.

class Registro (models.Model):
    fecha_registro = models.DateField(default=datetime, verbose_name="fecha de registro")
    nom_imagen =  models.CharField(max_length=100, verbose_name="Nombre de la imagen")
    id_usuario = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        db_table = "Registro"
        ordering = ["id"]

        




