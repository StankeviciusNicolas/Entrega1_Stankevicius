from django.shortcuts import render
from blog.models import Articulo, Autor, Seccion, Avatar
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from blog.forms import ArticuloFormulario, AvatarForm, UserEditionForm

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def about(request):
    return render(request, "about.html")


@login_required
def procesar_seccion(request):
    if request.method != "POST":
        return render(request, "agregar-seccion.html")

    seccion = Seccion(categoria=request.POST["categoria"], lugar=request.POST["lugar"])
    seccion.save()
    return render(request, "inicio.html")


@login_required
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


@login_required
def agregar_articulo(request):
    if request.method != "POST":
        miFormulario = ArticuloFormulario()

    else:
        miFormulario = ArticuloFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulo(
                titulo=informacion["titulo"],
                subtitulo=informacion["subtitulo"],
                fecha=informacion["fecha"],
                texto=informacion["texto"],
                imagen=informacion["imagen"],
            )
            articulo.save()
            return render(request, "inicio.html")

    contexto = {"formulario": miFormulario}
    return render(request, "agregar-articulo.html", contexto)


from django.urls import reverse


class ArticuloCreacion(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = "/articulo/list"
    fields = ["titulo", "subtitulo", "fecha", "texto", "imagen"]


class ArticuloDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = "articulo_detalle.html"


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = "/articulo/list"
    fields = ["titulo", "subtitulo", "fecha", "texto", "imagen"]


class ArticuloDelete(LoginRequiredMixin, DeleteView):

    model = Articulo
    success_url = "/articulo/list"


class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = "articulo_list.html"


#############################################


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


def leer_articulos(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos": articulos}
    return render(request, "leer-articulos.html", contexto)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "inicio.html", {"avatar": avatar.imagen.url})

    contexto = {"user": user, "form": form, "avatar": avatar.imagen.url}
    return render(request, "editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "inicio.html")

    contexto = {"form": form}
    return render(request, "avatar_form.html", contexto)


class ArticulosList(ListView):
    model = Articulo
    template_name = "templates/articulos_list.html"


class MyLogin(LoginView):
    template_name = "login.html"
