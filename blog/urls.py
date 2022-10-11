from django.urls import path
from blog.views import (
    inicio,
    buscar_articulo,
    buscar_autor,
    buscar_seccion,
    procesar_seccion,
    procesar_autor,
    procesar_articulo,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    path("agregar-seccion/", procesar_seccion, name="agregar-seccion"),
    path("agregar-autor/", procesar_autor, name="agregar-autor"),
    path("agregar-articulo/", procesar_articulo, name="agregar-articulo"),
    path("busqueda_autor/", buscar_autor, name="buscar_autor"),
    path("busqueda_articulo/", buscar_articulo, name="buscar_articulo"),
    path("busqueda_seccion/", buscar_seccion, name="bus car-seccion"),
]
