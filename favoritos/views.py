from django.shortcuts import render

# Create your views here.

def index_favoritos(request):
    return render(request, 'index.html')

def crear_favoritos(request):
    return render(request, 'favoritos/crear.html')