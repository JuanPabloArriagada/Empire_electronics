from django.urls import path

from empireapp.views import index, productos, detalleProducto, contacto, blog, about, registrarse, carrito, home, inventory, products, sales

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
]
