from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE
from Cart.models import CART
from django.db.models import Q

# Create your views here.

def Cart(request):
    products = PRODUCTS.objects.filter(Q(slug ='half-sleev-001')| Q(slug='half-sleev-006'))
    img = IMAGE.objects.filter(product__in=products)

    context ={

        'products':products,
        'img':img,
    }
    # return HttpResponse('Testing')
    return render(request,'Cart/cart.html',context)

def AddToProduct(request,product_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            producId = PRODUCTS.objects.get(id=product_id)
            print(f'productid is:{producId}')
            try:
                checkCart = CART.objects.get(product__slug=producId)
                checkCart.qty += 1
                checkCart.save()

                return JsonResponse({'status':'Success','message':'Cart added'})
            except:
                pass
        except:
            return JsonResponse({'status':'Failed','message':'Product not found'})
    else:
        return JsonResponse({'status':'Failed','message':'Invalid request'})
    