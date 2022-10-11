from django.shortcuts import render
from blog.models import Articulo, Autor, Seccion
from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def procesar_seccion(request):
    if request.method != "POST":
        return render(request, "agregar-seccion.html")

    seccion = Seccion(categoria=request.POST["categoria"], lugar=request.POST["lugar"])
    seccion.save()
    return render(request, "inicio.html")


def procesar_autor(request):
    if request.method != "POST":
        return render(request, "agregar-autor.html")

    autor = Autor(
        nombre=request.POST["nombre-autor"],
        apellido=request.POST["apellido-autor"],
        email=request.POST["email-autor"],
    )
    autor.save()
    return render(request, "inicio.html")


def procesar_articulo(request):
    if request.method != "POST":
        return render(request, "agregar-articulo.html")

    articulo = Articulo(
        titulo=request.POST["titulo-art"],
        fecha=request.POST["fecha-art"],
        texto=request.POST["texto-art"],
    )
    articulo.save()
    return render(request, "inicio.html")


def buscar_autor(request):
    if not request.GET["nombre"]:
        contexto = {"vacio": "No enviaste datos"}
        return render(request, "empty_form.html", contexto)
    else:
        nombre = request.GET["nombre"]
        autores = Autor.objects.filter(nombre__icontains=nombre)

        contexto = {
            "nombre": nombre,
            "autores": autores,
        }

        return render(request, "busqueda-autor.html", contexto)


def buscar_articulo(request):
    if not request.GET["titulo"]:
        contexto = {"vacio": "No enviaste datos"}
        return render(request, "empty_form.html", contexto)
    else:
        titulo = request.GET["titulo"]
        articulos = Articulo.objects.filter(titulo__icontains=titulo)

        contexto = {
            "titulo": titulo,
            "articulos": articulos,
        }

        return render(request, "busqueda-articulo.html", contexto)


def buscar_seccion(request):
    if not request.GET["categoria"]:
        contexto = {"vacio": "No enviaste datos"}
        return render(request, "empty_form.html", contexto)
    else:
        categoria = request.GET["categoria"]
        secciones = Seccion.objects.filter(categoria__icontains=categoria)

        contexto = {
            "categoria": categoria,
            "secciones": secciones,
        }

        return render(request, "busqueda-secciones.html", contexto)
