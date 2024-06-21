from django.shortcuts import get_object_or_404, render, redirect
from .forms import *

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

def products(request):
    return render(request, "empireapp/pages/dashboard/products.html")

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