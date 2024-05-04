from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE
from Cart.models import CART
from django.db.models import Q

# Create your views here.

def myCart(request):
    if request.user.is_authenticated:
        myProducts = CART.objects.filter(user=request.user)
    else:
        myProducts= None
    # products = PRODUCTS.objects.filter(Q(slug ='half-sleev-001')| Q(slug='half-sleev-006'))
    # img = IMAGE.objects.filter(product__in=products)

    context ={
        'myProducts':myProducts,
        # 'products':products,
        # 'img':img,
    }
    return render(request,'Cart/cart.html',context)
    