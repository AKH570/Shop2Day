from .models import CART
from Inventory.models import PRODUCTS,PRICE

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

# def cart_amt(request):
#     subtotal = 0
#     total = 0
#     if request.user.is_authenticated:
#         cartItems = CART.objects.filter(user=request.user)
#         for item in cartItems:
#             price = PRICE.objects.get(pk=item.product.id)
#             subtotal = (item.qty*price.mrp)
#             print(subtotal)
#     return dict(price=price)