from django.urls import path
from empireapp.views import *
from django.contrib.auth import views as auth_views

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
    path('pedidos/', pedidos, name="pedidos"),
    path('detallepedido/<int:pedido_id>/', detallepedido, name='detallepedido'),
    path('perfil/', perfil, name='perfil'),
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
    path('detalle_pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),
    path('crear_admin/', crear_admin, name='crear_admin'),

    
    #LOGIN Y LOGOUT
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    
    #CARRITO
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', cart_remove, name='cart_remove'),
    path('cart/update/<int:item_id>/', cart_update, name='cart_update'),
]
