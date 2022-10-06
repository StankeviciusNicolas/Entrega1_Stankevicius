from django.urls import path
from blog.views import inicio

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
]