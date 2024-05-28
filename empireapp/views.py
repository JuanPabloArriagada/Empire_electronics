from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"empireapp/index.html")

def productos(request):
    return render(request, "empireapp/pages/productos.html")