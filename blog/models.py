from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Autor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=250, null=True)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nombre + self.apellido


class Articulo(models.Model):

    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, null=True)
    fecha = models.DateField(null=True)
    texto = models.TextField(null=True)
    imagen = models.ImageField(upload_to="lugares", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Articulos"

    def __str__(self):
        return f"Título: {self.titulo} - Fecha: {self.fecha}"


class Seccion(models.Model):

    categoria = models.CharField(max_length=30)
    lugar = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Secciones"

    def __str__(self):
        return self.categoria


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
