from django.test import TestCase
from models import Articulo, Autor, Seccion


class ViewTestCase(TestCase):
    def test_crear_autor(self):
        Autor.objects.create(
            nombre="Pablo", apellido="Vegetti", email="pablito@gmail.com"
        )
        todos_los_autores = Autor.objects.all()
        assert len(todos_los_autores) == 1
        assert todos_los_autores[0].nombre == "Pablo"
        assert todos_los_autores[0].apellido == "Vegetti"
        assert todos_los_autores[0].email == "pablito@gmail.com"

        # def test_crear_curso_sin_fecha(self):
        #    Articulo.objects.create(nombre="test 1234", camada="9091")
        #    todos_los_articulos = Articulo.objects.all()
        #    assert todos_los_articulos[0].fecha_de_inicio is None

        # def test_crear_4_articulos(self):
        Seccion.objects.create(categoria="Seccion 01", lugar="1")
        Seccion.objects.create(categoria="Seccion 02", lugar="2")
        Seccion.objects.create(categoria="Seccion 03", lugar="3")
        Seccion.objects.create(categoria="Seccion 04", lugar="4")
        Seccion.objects.create(categoria="Seccion 05", lugar="5")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 4
