from django.urls import path

from .views import *
app_name = 'favoritos'

urlpatterns = [
    path('', index_favoritos)  # root
]