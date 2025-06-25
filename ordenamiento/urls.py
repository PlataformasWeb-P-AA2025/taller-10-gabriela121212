from django.urls import path
from . import views

urlpatterns = [
    path('', views.parroquias_con_barrios, name='inicio'),
    path('barrios/<int:id>/', views.lista_barrios, name='barrios'),
    path('parroquia/nueva/', views.crear_parroquia, name='crear_parroquia'),
    path('barrio/nuevo/', views.crear_barrio, name='crear_barrio'),
]

