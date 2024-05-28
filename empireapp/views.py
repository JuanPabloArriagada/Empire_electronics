from django.shortcuts import render

# Create your views here.
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