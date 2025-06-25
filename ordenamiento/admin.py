from django.contrib import admin

# Register your models here.

#[<a href="{% url 'crear_parroquia' %}">Agregar Parroquia</a>]
#[<a href="{% url 'crear_barrio' %}">Agregar Barrio</a>]
#[<a href="{% url 'editar_parroquia' parroquia.id %}">Editar</a>]
#[<a href="{% url 'eliminar_parroquia' parroquia.id %}">Eliminar</a>]

from .models import Parroquia, Barrio

admin.site.register(Parroquia)
admin.site.register(Barrio)