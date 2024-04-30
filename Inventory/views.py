from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.contrib import messages
from Inventory.models import (
                PRODUCTS,IMAGE,ATTRIBUTES,STOCKS,
                PRICE,ATTRIBUTEVALUE,SUBCATEGORY)
from Category.models import CATEGORY
from Review.models import Reviews
from Review.forms import ReviewForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from Cart.models import CART
import json
# Create your views here.

# def Store(request):
#     categorys = CATEGORY.objects.filter(slug__in=['popular-product','new-arrival'])
#     #singlecate = allCategory.get(slug='all-item')
#     products = PRODUCT.objects.filter(category__slug='all-item').exclude(slug='side-photo')
#     #sidephoto = PRODUCT.objects.filter(slug='side-photo')
#     paginator = Paginator(products,3)
#     pageNumber = request.GET.get("page")
#     pageProduct = paginator.get_page(pageNumber)
#     allcount = products.count()
#     context={      'products':pageProduct,
#                    'productCount':allcount,
#                    #'sidephoto':sidephoto,
#                    'cateAll':categorys}
    
#     return render(request,'Store/store.html',context)

#In Product Menu the first slug-Summer Stor
"""
def categoryOne(request,category_slug=None,subcate_slug=None):
    products = None
    categories = None
    if category_slug is not None and subcate_slug is not None:
        categories = get_object_or_404(CATEGORY,slug = category_slug)
        subcategoris = get_object_or_404(SUBCATEGORY,slug =subcate_slug,category=categories)
        print(f'subcate:{subcategoris}')
        #products= PRODUCTS.objects.filter(category=categories)
        products= PRODUCTS.objects.filter(subcategory=subcategoris)
        productImg=IMAGE.objects.filter(product__in=products)
        print(f'productImg:{productImg}')
        colorattr = ATTRIBUTEVALUE.objects.filter(attribute__name='Color')
        sizeattr = ATTRIBUTEVALUE.objects.filter(attribute__name='Size')
        colorid = request.GET.get('color')
        if colorid:
             productImg=IMAGE.objects.filter(product__attributevalue=colorid,
                                            product__category=categories)
        
        else:
            productImg=IMAGE.objects.filter(product__in=products)
        #sidephoto = PRODUCT.objects.filter(slug='side-banner-1')
        #allCategory = CATEGORY.objects.all().exclude(slug__in=['new-arrival','popular-product','all-item'])
        # paginator = Paginator(products,3)
        # pageNumber = request.GET.get("page")
        # pageProduct = paginator.get_page(pageNumber)
        productCount = products.count()
        context = { 'products':products,
                    'productImg':productImg,
                    'colorattr':colorattr,
                    'sizeattr':sizeattr,
                    'productCount':productCount
                     }
    else:
        pass
    return render(request,'Inventory/productCate1.html',context )

# def FilterByColor(request,cate_slug,color_name):
#      products = PRODUCTS.objects.filter(category__slug=cate_slug)
#      colorproduct = COLORS.objects.filter(product__category__slug=cate_slug,name=color_name)
#      print(f'color:{colorproduct}')
#      #ChooseProduct = PRODUCTS.objects.filter(category__slug=cate_slug)
#      #return HttpRequest('hello')
#      return render(request,'Inventory/productCate1.html')
"""

def productDetails(request,cate_slug,prod_slug):
        ChooseProduct = get_object_or_404(PRODUCTS,category__slug=cate_slug,slug=prod_slug)
        ProductImg = IMAGE.objects.get(product=ChooseProduct)
        price = PRICE.objects.get(product=ChooseProduct)
        stocks = STOCKS.objects.get(product=ChooseProduct)
        attributes = ATTRIBUTEVALUE.objects.all()
        releteImg = IMAGE.objects.all()
        reviews = Reviews.objects.filter(product=ChooseProduct)
        # if ChooseProduct.is_discount==True:
        #      tag_price = round(price.saleprice - (price.saleprice*price.discount_percentage)/100,2)
        # else:
        #      tag_price = price.saleprice
        #      print(f'tagprice:{tag_price}')
        context = {'viewproduct':ChooseProduct,
                'img':ProductImg,
                'price':price,
                'stocks':stocks,
                'releted_img':releteImg,
                'attributes':attributes,
                'reviews':reviews,
                }
        return render(request,'Inventory/productDetail.html',context)

@login_required
def UserReviews(request,cate_slug,prod_slug):
    ChooseProduct = get_object_or_404(PRODUCTS,category__slug=cate_slug,slug=prod_slug)
    if request.method == 'POST':
        forms = ReviewForm(request.POST or None)
        # print(f'form:{forms}')
        if forms.is_valid():
            rating = forms.cleaned_data['rating']
            message = request.POST.get('new_review')
            # comments = forms.cleaned_data.get('my_review',None)
            author = request.user
            ip = request.META.get('REMOTE_ADDR')
            product = ChooseProduct
            create_review = Reviews.objects.create(author=author,product=product,message=message,rating=rating,ip=ip)
            create_review.save()
            messages.success(request, 'Successfully reviewed product')
            return HttpResponseRedirect(reverse('productDetails', args=(product.category.slug,product.slug, )))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        return render(request,'Inventory/productDetail.html',context)

def AddProduct(request,cate_slug,prod_slug):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                ChooseProduct = PRODUCTS.objects.get(category__slug=cate_slug,slug=prod_slug)
                # check wether this product is already in cart
                try:
                    productIncart = CART.objects.get(user=request.user,product=ChooseProduct)
                    productIncart.qty += 1
                    productIncart.save()
                    return JsonResponse({'status':'Success','message':'Product increased'})
                except:
                    productIncart = CART.objects.create(user=request.user,product=ChooseProduct,qty=1)
                    return JsonResponse({'status':'Success','message':'Product added'})
            except:
                return JsonResponse({'status':'Failed','message':'This product is not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid request'})
    else:
        return JsonResponse({'status':'Failed','message':'Please login'})
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     try:
    #         producId = PRODUCTS.objects.get(id=product_id)
    #         print(f'productid is:{producId}')
    #         try:
    #             checkCart = CART.objects.get(product__slug=producId)
    #             checkCart.qty += 1
    #             checkCart.save()

    #             return JsonResponse({'status':'Success','message':'Cart added'})
    #         except:
    #             pass
    #     except:
    #         return JsonResponse({'status':'Failed','message':'Product not found'})
    # else:
    #     return JsonResponse({'status':'Failed','message':'Invalid request'})
    