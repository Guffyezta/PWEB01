from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html = "<html><body>Harrys eres genial</body></html>"
    return HttpResponse(html)


def galeria_html(request):
    html = "<html><body>Galeria Html</body></html>"
    return HttpResponse(html)

def galeria_orig(request):
    return render(request, 'galeria.html')

def galeria_json(request):
    return render(request, 'galeria_json.html')

def galeria_json_login(request):
    return render(request, 'galeria_json_login.html')

def galeria_carrusel(request):
    return render(request, 'galeria_carrusel.html')

def galeria_modal(request):
    return render(request, 'galeria_modal.html')

from django.template import loader
def index(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())


def empleados(request):
   template = loader.get_template('empleados.html')
   return HttpResponse(template.render())   

def empleadosJson(request):
   template = loader.get_template('empleadosJson.html')
   return HttpResponse(template.render())   

def clientes(request):
   template = loader.get_template('clientes.html')
   return HttpResponse(template.render()) 

        
def productos(request):
   template = loader.get_template('productos.html')
   return HttpResponse(template.render()) 

def regiones(request):
   template = loader.get_template('regiones.html')
   return HttpResponse(template.render())              