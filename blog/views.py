from django.shortcuts import render
from blog.models import Articulo, Autor, Seccion

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")

def bienvenida(request):
    return render(request, "bienvenida.html")

def procesar_seccion(request):
    if request.method != "POST":
        return render(request, "agregar-seccion.html")
    
    seccion1 = Seccion(categoria=request.POST["categoria"], lugar=request.POST["lugar"])
    seccion1.save()

    return render(request, "inicio.html")

    