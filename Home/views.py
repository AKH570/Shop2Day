from django.shortcuts import render
from Inventory.models import (
    PRODUCTS,IMAGE,PRICE,BRAND,SUBCATEGORY,STOCKS)
from Category.models import CATEGORY
from django.http import HttpResponse
from django.db.models import Q

#hsl(214, 42%, 46%);
# Create your views here.
def home(request):
    popularsubcategorys = SUBCATEGORY.objects.filter(slug__exact='popular-items')
    flashsubcategorys = SUBCATEGORY.objects.filter(slug__exact='flash-sale')
    # print(f'subcate:{subcategorys}')
    popularProd = PRODUCTS.objects.filter(subcategory__in=popularsubcategorys)
    flashProd = PRODUCTS.objects.filter(subcategory__in=flashsubcategorys)
    # print(f'new:{newarrProd}')
    #flashProducts = PRODUCTS.objects.filter(category=CATEGORY.objects.get(slug='popular'),is_active=True)
    #price = PRICE.objects.filter(product__in=newarrProd)
    #print(f'price:{price}')
    #brands = BRAND.objects.all()
    PopularProdImage = IMAGE.objects.filter(product__in=popularProd)
    flashProdImage = IMAGE.objects.filter(product__in=flashProd)
    #flashprodImg = IMAGE.objects.filter(product__in=flashProducts)

    stocks = STOCKS.objects.filter(product__in=popularProd)

    context = {
        'NewProdImage':PopularProdImage,
        'flashProdImg':flashProdImage,
        'stocks':stocks,
    }
    return render(request,'Home/index.html',context)

def search(request):
    if 'keyword' in request.GET:
          keyword   = request.GET['keyword']
          if keyword:
               products=PRODUCTS.objects.order_by('-create_date').filter(name__icontains=keyword)
               print(f'name:{products}')
               products_Img=IMAGE.objects.filter(product__name__icontains=keyword)
               print(f'Img:{products_Img}')
    context={
         'NewProdImage':products_Img,
    }

    return render(request,'Home/index.html',context)