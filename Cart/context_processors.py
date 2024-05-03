from .models import CART

def get_cart_items(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        try:
            cart_items = CART.objects.filter(user=request.user)
            if cart_items:
                for cart_item in cart_items:
                    items_in_cart += cart_item.qty
            else:
                items_in_cart=0
        except:
            items_in_cart=0
    return dict(items_in_cart=items_in_cart)