from django.shortcuts import render
from Inventory.models import (
    PRODUCTS,IMAGE,PRICE,BRAND,SUBCATEGORY,STOCKS)
from Category.models import CATEGORY
from django.http import HttpResponse
from django.db.models import Q

#hsl(214, 42%, 46%);
# Create your views here.
def home(request):
    homeItems = SUBCATEGORY.objects.filter(slug__exact='baby-boy-item')
    flashsubcategorys = SUBCATEGORY.objects.filter(slug__exact='flash-sale')
    # print(f'subcate:{subcategorys}')
    newProd = PRODUCTS.objects.filter(subcategory__in=homeItems)
    flashProd = PRODUCTS.objects.filter(subcategory__in=flashsubcategorys)
    # print(f'new:{newarrProd}')
    #flashProducts = PRODUCTS.objects.filter(category=CATEGORY.objects.get(slug='popular'),is_active=True)
    #price = PRICE.objects.filter(product__in=newarrProd)
    #print(f'price:{price}')
    #brands = BRAND.objects.all()
    newProdImage = IMAGE.objects.filter(product__in=newProd)
    flashProdImage = IMAGE.objects.filter(product__in=flashProd)
    #flashprodImg = IMAGE.objects.filter(product__in=flashProducts)

    stocks = STOCKS.objects.filter(product__in=newProd)

    context = {
        'products':newProdImage,
        'flashProdImg':flashProdImage,
        'stocks':stocks,
    }
    return render(request,'Home/index.html',context)

# def mensItem(request):
#     mensproducts = PRODUCTS.objects.filter(category=CATEGORY.objects.get(slug='men'))
#     print(f'mens:{mensproducts}')

def search(request):
    if 'keyword' in request.GET:
          keyword   = request.GET['keyword']
          if keyword:
               products=PRODUCTS.objects.order_by('-create_date').filter(Q(name__icontains=keyword)|Q(description__icontains=keyword)|Q(slug__icontains=keyword))
               products_Img=IMAGE.objects.filter(product__in=products)
    context={
         'products':products_Img,
    }

    return render(request,'Home/index.html',context)