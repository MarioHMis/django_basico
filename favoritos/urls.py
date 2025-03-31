from django.urls import path

from .views import *

app_name = 'favoritos'

urlpatterns = [
    path('', index_favoritos, name='index'),
    path('crear', crear_favoritos),
    path('borrar/<int:pk>', borrar_favoritos,name='borrar'),
]