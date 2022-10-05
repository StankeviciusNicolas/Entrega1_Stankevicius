from django.db import models

# Create your models here.


class Autor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.apellido


class Articulo(models.Model):

    titulo = models.CharField(max_length=50)
    fecha = models.DateField(null=True)
    texto = models.TextField(null=True)
    imagen = models.ImageField(upload_to="imagenes/",null=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.titulo


class Seccion(models.Model):

    categoria = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"

    def __str__(self):
        return self.categoria
