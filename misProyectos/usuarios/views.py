from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'usuarios/index.html', context)

def contacto(request):
    context={}
    return render(request, 'usuarios/contacto.html', context)

def donacion(request):
    context={}
    return render(request, 'usuarios/donacion.html', context)

def nosotros(request):
    context={}
    return render(request, 'usuarios/nosotros.html', context)

def seccion_gato(request):
    context={}
    return render(request, 'usuarios/seccion_gato.html', context)

def seccion_perro(request):
    context={}
    return render(request, 'usuarios/seccion_perro.html', context)

def tienda(request):
    context={}
    return render(request, 'usuarios/tienda.html', context)