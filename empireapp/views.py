from django.shortcuts import render, redirect
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

#VIEWS DE LOS FORMS
def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='clientes')  # Replace with your success URL
    else:
        form = ClienteForm()
    return render(request, 'template_name.html', {'form': form})