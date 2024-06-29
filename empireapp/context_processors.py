
from empireapp.models import Cart, CartItem
from django.contrib.auth.forms import AuthenticationForm


def cart_item_count(request):
    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            cart_item_count = cart_items.count()
    return {'cart_item_count': cart_item_count}


def login_form(request):
    # Inicializar el formulario de inicio de sesión
    form = AuthenticationForm()
    return {'login_form': form}