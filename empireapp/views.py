import os
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from os import  remove
from django.conf import settings
# Create your views here.
#PAGES
def index(request):
    return render(request, "empireapp/index.html")

def productos(request):
    return render(request, "empireapp/pages/productos.html")

def detalleProducto(request):
    return render(request, "empireapp/pages/detalleProducto.html")

def contacto(request):
    return render(request, "empireapp/pages/contact.html")

def blog(request):
    return render(request, "empireapp/pages/blog.html")

def about(request):
    return render(request, "empireapp/pages/about.html")

def registrarse(request):
    return render(request, "empireapp/pages/registrarse.html")

def carrito(request):
    return render(request, "empireapp/pages/carrito.html")

#DASHBOARD
def home(request):
    return render(request, "empireapp/pages/dashboard/home.html")

def inventory(request):
    return render(request, "empireapp/pages/dashboard/inventory.html")

def sales(request):
    return render(request, "empireapp/pages/dashboard/sales.html")

def clientes(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, "empireapp/pages/dashboard/clientes.html", datos)

def detallecliente(request, id):
    cliente=get_object_or_404(Cliente, rut=id)
    datos={
        "cliente":cliente
    }
    return render(request, "empireapp/pages/dashboard/detallecliente.html", datos)

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
def añadircelulares(request):
    form=CelularesForms()

    if request.method=="POST":
        form=CelularesForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            """ messages.success(request, 'Laptop agregada') """
            return redirect(to="products")

    datos={
        "form":form
    }
    return render(request, "empireapp/pages/dashboard/añadircelulares.html",datos)


def products(request):
    laptops = Laptops.objects.all()
    celulares = Celulares.objects.all()
    
    productos = {
        'laptops': laptops,
        'celulares': celulares
    }
    
    print(productos)
    return render(request,"empireapp/pages/dashboard/products.html", productos)



def editarproducto(request, product_type, pk):
    if product_type == 'laptop':
        product = get_object_or_404(Laptops, id=pk)
        form = UpdateLaptopsForm(request.POST or None, instance=product)
    elif product_type == 'celular':
        product = get_object_or_404(Celulares, id=pk)
        form = UpdateCelularesForm(request.POST or None, instance=product)
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