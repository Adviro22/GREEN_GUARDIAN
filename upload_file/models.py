from django.db import models
from datetime import datetime
from show_result.models import Planta, Plaga

# Create your models here.

class Registro (models.Model):
    fecha_registro = models.DateField(default=datetime, verbose_name="fecha de registro")
    nom_imagen =  models.CharField(max_length=100, verbose_name="Nombre de la imagen")
    imagen_binaria = models.BinaryField(blank=True, null=True)
    id_usuario = models.IntegerField()
    plaga = models.CharField( default='',max_length=100000)
    cultivo = models.CharField( default='', max_length=100000)
    # plaga =  models.ForeignKey(Plaga, on_delete=models.CASCADE, verbose_name='Tipo de Planta')
    # cultivo =  models.ForeignKey(Planta, on_delete=models.CASCADE, verbose_name='Tipo de plaga')

    def __str__(self):
        return f"img_binaria: {self.imagen_binaria}, Nombre de Imagen: {self.nom_imagen}, Fecha de Registro: {self.fecha_registro}, Usuario ID: {self.id_usuario}, Plaga: {self.plaga}, Cultivo: {self.cultivo}"
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        db_table = "Registro"
        ordering = ["id"]





