from django.urls import path

from empireapp.views import index, productos, detalleProducto, contacto, blog, about, registrarse

#URLS DE APLICACION
urlpatterns = [
    path('', index, name='index'), 
    path('productos/', productos, name="productos"),
    path('detalleProducto/', detalleProducto, name="detalleProducto"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('about/', about, name="about"),
    path('registrarse/', registrarse, name="registrarse"),
]
