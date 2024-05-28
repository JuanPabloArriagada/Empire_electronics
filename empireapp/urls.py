from django.urls import path

from empireapp.views import index, productos

#URLS DE APLICACION
urlpatterns = [
    path('', index, name='index'), 
    path('productos/', productos, name="productos"),
]
