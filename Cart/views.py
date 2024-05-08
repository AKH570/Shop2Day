from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE
from Cart.models import CART
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from Cart.context_processors import get_cart_items

# Create your views here.
@login_required(login_url='login')
def myCart(request):
        myCart = CART.objects.filter(user=request.user)

    # products = PRODUCTS.objects.filter(Q(slug ='half-sleev-001')| Q(slug='half-sleev-006'))
    # img = IMAGE.objects.filter(product__in=products)

        context ={
            'myCart':myCart,
            # 'products':products,
            # 'img':img,
        }
        return render(request,'Cart/mycart.html',context)

def deleteCart(request, cartId):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                #ChooseProduct = PRODUCTS.objects.get(slug=prod_slug)
                cartItems = CART.objects.get(user=request.user,id=cartId)
                print(f'cartid : {cartItems}')
                if cartItems:
                    cartItems.delete()
                    return JsonResponse({'status':'Success','message':'Your Cart Item is deleted','cartCount':get_cart_items(request)})
            except:
                return JsonResponse({'status':'Success','message':'Your Cart Item is deleted'})
                #return JsonResponse({'status':'Failed','message':'Cart item dose not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid request'})
    
    