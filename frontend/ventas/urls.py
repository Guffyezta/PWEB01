from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='post_list'),
    path('index', views.index, name='post_list'),
    path('productos', views.productos, name='post_list'),
    path('empleados', views.empleados, name='post_list'),
    path('regionListJson', views.empleadosJson, name='post_list'),
    path('clientes', views.clientes, name='post_list'),
    path('regiones', views.regiones, name='post_list'),

    path('galeria_html', views.galeria_html, name='post_list'),
    path('galeria_html_orig', views.galeria_orig, name='post_list'),
    path('galeria_json', views.galeria_json, name='post_list'),
    path('galeria_json_login', views.galeria_json_login, name='post_list'),
    path('galeria_carrusel', views.galeria_carrusel, name='post_list'),
    path('galeria_modal', views.galeria_modal, name='post_list'),
]