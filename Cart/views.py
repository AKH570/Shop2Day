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
    #Product_price = []
    myCart = CART.objects.filter(user=request.user)
    # qn = PRICE.objects.get(product= i.product for i in myCart)
    print(myCart)
    # price = PRICE.objects.filter(product=myCart.product)
    # print(price)
    # if myCart:
    #     for i in myCart:
    #         price = PRICE.objects.get(product=i.product)
            # Qnty = i.qty
            # product = i.product
            # Product_price.qnty_price = i.qty*price.mrp

        
    context ={
        'myCart':myCart,
        # 'price':price,
    }
    return render(request,'Cart/mycart.html',context)

def deleteCart(request, cartId):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                #ChooseProduct = PRODUCTS.objects.get(slug=prod_slug)
                cartItems = CART.objects.get(user=request.user,id=cartId)
                #print(f'cartid : {cartItems}')
                if cartItems:
                    cartItems.delete()
                    return JsonResponse({'status':'Success','message':'Your Cart Item is deleted','cartCount':get_cart_items(request)})
            except:
                return JsonResponse({'status':'Success','message':'Your Cart Item is deleted'})
                #return JsonResponse({'status':'Failed','message':'Cart item dose not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid request'})
    
    