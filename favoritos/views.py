from django.shortcuts import render
from .models import Favoritos

# Create your views here.

def index_favoritos(request):
    return render(request, 'index.html')

def crear_favoritos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        url = request.POST['url']
        Favoritos.objects.create(nombre=nombre, url=url)
       
    return render(request, 'favoritos/crear.html')