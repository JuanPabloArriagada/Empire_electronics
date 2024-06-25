from django.urls import path
from empireapp.views import *

#URLS DE APLICACION
urlpatterns = [
    #PAGINA
    path('', index, name='index'), 
    path('productos/', productos, name="productos"),
    path('detalleProducto/', detalleProducto, name="detalleProducto"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('about/', about, name="about"),
    path('registrarse/', registrarse, name="registrarse"),
    path('carrito/', carrito, name="carrito"),
    #ADMIN
    path('home/', home, name="home"),
    path('inventory/', inventory, name="inventory"),
    path('products/', products, name="products"),
    path('sales/', sales, name="sales"),
    path('clientes/', clientes, name="clientes"),
    path('detallecliente/<id>', detallecliente, name="detallecliente"),
    path('crearcliente/',crearcliente,name='crearcliente'),
    path('modificarcliente/<id>',modificarcliente, name='modificarcliente'),
    path('eliminarcliente/<id>', eliminarcliente, name='eliminarcliente'),
    path('añadirlaptops/', añadirlaptops, name="añadirlaptops"),
    path('añadircelulares/', añadircelulares, name="añadircelulares"),
    path('editarproducto/<str:product_type>/<int:pk>', editarproducto, name="editarproducto"),
    path('eliminar_producto/<str:product_type>/<int:pk>', eliminar_producto, name="eliminar_producto"),
]
