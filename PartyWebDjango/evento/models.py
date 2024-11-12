from datetime import timezone
from django.db import models

# Create your models here.


class Evento(models.Model):
    nombre = models.CharField(max_length=100, default="Sin especificar")
    
    slide_foto1 = models.ImageField(upload_to='media/', blank=True, null=True)
    slide_foto2 = models.ImageField(upload_to='media/', blank=True, null=True)
    slide_foto3 = models.ImageField(upload_to='media/', blank=True, null=True)
    
    header_titulo = models.CharField(max_length=100, default="Sin especificar")
    header_descripcion = models.TextField()
    header_foto_fondo = models.ImageField(upload_to='media/', blank=True, null=True)
    
    fecha = models.DateField()
    content1_foto_fondo = models.ImageField(upload_to='media/', blank=True, null=True)
    content1_titulo = models.CharField(max_length=100, default="Sin especificar")
    content1_lugar = models.CharField(max_length=100, default="Sin especificar")
    content1_direccion_lugar = models.CharField(max_length=100, default="No especificada")
    content1_ciudad_lugar = models.CharField(max_length=100)
    content1_hora = models.CharField(max_length=50, null=True)
    
    galeria_foto1 = models.ImageField(upload_to='media/', blank=True, null=True)
    galeria_foto2 = models.ImageField(upload_to='media/', blank=True, null=True)
    galeria_foto3 = models.ImageField(upload_to='media/', blank=True, null=True)
    galeria_foto4 = models.ImageField(upload_to='media/', blank=True, null=True)
    
    link_mapa = models.URLField(max_length=200, blank=True, null=True)
    playlist_url = models.URLField(max_length=200, blank=True, null=True)
    imagen_1 = models.ImageField(upload_to='media/', blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='media/', blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.header_titulo