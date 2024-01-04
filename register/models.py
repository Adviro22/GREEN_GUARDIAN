
from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password

# Create your models here.

class user_register(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    user_name = models.CharField(max_length=100, verbose_name='Nombre_Usuario')
    e_mail = models.CharField(max_length=50, verbose_name='Correo')
    password = models.CharField(max_length=120, verbose_name='Contraseña')
    creation_date = models.DateField(default=datetime.now, verbose_name='fecha_creacion')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'User_Register'
        verbose_name_plural = 'Users_Register'
        db_table = 'User_Register'
        ordering = ['id']
# Create your models here.
