from django.urls import path
from blog.views import bienvenida, procesar_seccion, inicio

urlpatterns = [
    path("", bienvenida, name="bienvenida"),
    path("inicio/", inicio, name="inicio"),
    path("agregar-seccion/", procesar_seccion, name="agregar-seccion")
]