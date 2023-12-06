from django.db import models
from datetime import datetime
# Create your models here.

class user_login(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    user_name = models.CharField(max_length=100, verbose_name='Nombre_Usuario')
    e_mail = models.CharField(max_length=50, verbose_name='Correo')
    password = models.CharField(max_length=120, verbose_name='Contraseña')
    creation_date = models.DateField(default=datetime.now, verbose_name='fecha_creacion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User_Login'
        verbose_name_plural = 'Users_Login'
        db_table = 'User_login'
        ordering = ['id']

