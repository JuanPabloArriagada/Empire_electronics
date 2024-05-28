from django.urls import path

from empireapp.views import index, productos, detalle_producto, contacto, blog, about

#URLS DE APLICACION
urlpatterns = [
    path('', index, name='index'), 
    path('productos/', productos, name="productos"),
    path('detalle-producto/', detalle_producto, name="detalle-producto"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('about/', about, name="about"),
]
