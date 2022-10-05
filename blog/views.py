from select import select
from django.http import HttpResponse
from django.template import loader

from blog.models import Articulo, Autor, Seccion

# Create your views here.


def inicio(request):

    template = loader.get_template("inicio.html")
    articulos = Articulo.objects.all()
    diccionario = {"articulo1":1}

    res = template.render(diccionario)
    return HttpResponse(res)