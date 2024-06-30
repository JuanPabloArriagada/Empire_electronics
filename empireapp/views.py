import os
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from os import  remove
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Sum
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
#PAGES
def index(request):
    cart_item_count = 0
    items = []
    total = 0

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart).select_related('producto')
        cart_item_count = cart_items.count()
        items = cart_items
        total = sum(item.producto.precio * item.quantity for item in items)
    else:
        cart = None

    context = {
        'cart_item_count': cart_item_count,
        'cart': cart,
        'items': items,
        'total': total,
        'login_form': AuthenticationForm()
    }

    return render(request, 'empireapp/index.html', context)

def productos(request):
    productos = Producto.objects.all()
    
    lista_productos = {
        'productos': productos,
    }
    
    return render(request, "empireapp/pages/productos.html",lista_productos)

def detalleProducto(request):
    return render(request, "empireapp/pages/detalleProducto.html")

def contacto(request):
    return render(request, "empireapp/pages/contact.html")

def blog(request):
    return render(request, "empireapp/pages/blog.html")

def about(request):
    return render(request, "empireapp/pages/about.html")

def registrarse(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'empireapp/pages/registrarse.html', {'form': form})

@login_required
def pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user)
    return render(request, 'empireapp/pages/pedidos.html', {'pedidos': pedidos})

def detallepedido(request, pedido_id):
    detalle_pedido = PedidoItem.objects.filter(pedido_id = pedido_id)
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    return render(request, 'empireapp/pages/detallepedido.html', {'productos': detalle_pedido, 'pedido':pedido})
#DASHBOARD
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def crear_admin(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página deseada después de crear el admin
    else:
        form = AdminCreationForm()
    
    return render(request, 'empireapp/pages/dashboard/crear_admin.html', {'form': form})
@user_passes_test(is_admin)

def home(request):
    return render(request, "empireapp/pages/dashboard/home.html")

@user_passes_test(is_admin)
def inventory(request):
    productos = Producto.objects.all()
    
    lista_productos = {
        'productos': productos,
    }
    return render(request, "empireapp/pages/dashboard/inventory.html", lista_productos)

@user_passes_test(is_admin)
def sales(request):
    pedidos = Pedido.objects.annotate(
        total_productos=Sum('items__cantidad')
    ).select_related('user')
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        nuevo_estado = request.POST.get('estado')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        if nuevo_estado and nuevo_estado in dict(TIPO_ESTADO_PEDIDO):
            pedido.estado = nuevo_estado
            pedido.save()
            return redirect('sales')

    context = {
        'pedidos': pedidos,
        'tipo_estado_pedido': TIPO_ESTADO_PEDIDO,
    }
    return render(request, "empireapp/pages/dashboard/sales.html", context)

@user_passes_test(is_admin)
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalle_pedido = PedidoItem.objects.filter(pedido_id=pedido_id).select_related('producto')
    
    context = {
        'pedido': pedido,
        'detalle_pedido': detalle_pedido
    }
    return render(request, 'empireapp/pages/dashboard/detalle_pedido.html', context)

@user_passes_test(is_admin)
def clientes(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, "empireapp/pages/dashboard/clientes.html", datos)

@user_passes_test(is_admin)
def detallecliente(request, id):
    cliente=get_object_or_404(Cliente, rut=id)
    datos={
        "cliente":cliente
    }
    return render(request, "empireapp/pages/dashboard/detallecliente.html", datos)

@user_passes_test(is_admin)
def crearcliente(request):
    form=ClienteForm()

    if request.method=="POST":
        form=ClienteForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            """ messages.success(request, 'Persona agregada al registro') """
            return redirect(to="clientes")

    datos={
        "form":form
    }
    return render(request, "empireapp/pages/dashboard/crearcliente.html", datos)

@user_passes_test(is_admin)
def modificarcliente(request,id):
    cliente=get_object_or_404(Cliente,rut=id)

    form=UpdateClienteForm(instance=cliente)
    datos={
        "form":form,
        "cliente":cliente
    }

    if request.method=="POST":
        form=UpdateClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            """ messages.warning(request,'cliente Modificada') """
            return redirect(to='clientes')
        
    return render(request, "empireapp/pages/dashboard/modificarcliente.html", datos)

@user_passes_test(is_admin)
def eliminarcliente(request,id):
    cliente=get_object_or_404(Cliente,rut=id)

    datos={
        "cliente":cliente
    }

    if request.method=="POST":
        cliente.delete()
        """ messages.error(request, 'cliente Eliminado') """
        return redirect(to='clientes')
    return render(request, "empireapp/pages/dashboard/eliminarcliente.html", datos)

#LAPTOPS
@user_passes_test(is_admin)
def añadirlaptops(request):
    form=LaptopsForm()

    if request.method=="POST":
        form=LaptopsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            """ messages.success(request, 'Laptop agregada') """
            return redirect(to="products")

    datos={
        "form":form
    }
    return render(request, "empireapp/pages/dashboard/añadirlaptops.html", datos)


#CELULARES
@user_passes_test(is_admin)
def añadircelulares(request):
    form=CelularesForm()

    if request.method=="POST":
        form=CelularesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            """ messages.success(request, 'Laptop agregada') """
            return redirect(to="products")

    datos={
        "form":form
    }
    return render(request, "empireapp/pages/dashboard/añadircelulares.html",datos)


@user_passes_test(is_admin)
def products(request):
    productos = Producto.objects.all()
    
    lista_productos = {
        'productos': productos,
    }
    
    return render(request, "empireapp/pages/dashboard/products.html", lista_productos)

@user_passes_test(is_admin)
def editarproducto(request, product_type, pk):
    if product_type == 'laptop':
        product = get_object_or_404(Laptops, id=pk)
        form = LaptopsForm(request.POST or None, instance=product)
    elif product_type == 'celular':
        product = get_object_or_404(Celulares, id=pk)
        form = CelularesForm(request.POST or None, instance=product)
    else:
        # Handle unknown product type
        return redirect('products')

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('products')

    context = {
        'form': form,
        'product_type': product_type,
    }
    return render(request, "empireapp/pages/dashboard/editarproducto.html", context)

@user_passes_test(is_admin)
def eliminar_producto(request, product_type, pk):
    if product_type == 'laptop':
        product = get_object_or_404(Laptops, id=pk)
            
    elif product_type == 'celular':
        product = get_object_or_404(Celulares, id=pk)
        
    else:
        # Manejar caso de product_type desconocido o incorrecto
        return redirect('products')  # Redirigir a la página de productos o donde corresponda

    if request.method == 'POST':
        if product.imagen:
            remove(os.path.join(str(settings.MEDIA_ROOT).replace('/media','')+product.imagen.url))
        product.delete()
        return redirect('products')  # Redirigir a la página de productos después de eliminar

    context = {
        'product': product,
        'product_type': product_type,
    }
    return render(request, "empireapp/pages/dashboard/eliminar_producto.html", context)

#CARRITO
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart).select_related('producto')
    
    total = sum(item.producto.precio * item.quantity for item in items)
    
    if request.method == 'POST':
        with transaction.atomic():
            # Crear el objeto Pedido
            pedido = Pedido.objects.create(
                user=request.user,
                total=total,
                estado='pendiente'
            )
            
            # Iterar sobre los items del carrito y agregarlos al pedido
            for item in items:
                pedido_item = PedidoItem.objects.create(
                    pedido=pedido,
                    producto=item.producto,
                    cantidad=item.quantity
                )
            
            # Vaciar el carrito después de completar el pedido
            cart.cartitem_set.all().delete()
            cart.delete()
        return redirect('pedidos')
    return render(request, 'cart/detail.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        item, created = CartItem.objects.get_or_create(cart=cart, producto=product)
        item.quantity += cd['quantity']
        item.save()
    return redirect('cart_detail')

@login_required
def cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    print(item)
    return redirect('cart_detail')

@login_required
def cart_update(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'incrementar':
            item.quantity += 1
            item.save()
        elif action == 'decrementar':
            if item.quantity > 1:
                item.quantity -= 1
                item.save()
            else:
                # Si la cantidad es 1 y se intenta decrementar, eliminar el producto del carrito
                item.delete()

    return redirect('cart_detail')