from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE
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
    # data = {'message': 'Hello, World!'}
    return HttpResponse('Testing')
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     try:
    #         product = PRODUCTS.objects.get(slug=product_slug)
    #         print(f'product{product}')
    #     except:
    #         return JsonResponse({'status':'Failed','message':'Product Not found'})
    # else:
    #     return JsonResponse({'status':'Failed','message':'Invalid Reques'})

#check product is already exist in cart     
    #return HttpResponse('Testing')