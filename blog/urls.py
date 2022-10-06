from django.urls import path
from blog.views import bienvenida, inicio

urlpatterns = [
    path("", bienvenida, name="bienvenida"),
    path("inicio/", inicio, name="inicio"),
]