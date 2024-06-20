from django.shortcuts import render,get_object_or_404,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib import messages
from Inventory.models import (
                PRODUCTS,IMAGE,ATTRIBUTES,STOCKS,
                PRICE,ATTRIBUTEVALUE,SUBCATEGORY)
from Category.models import CATEGORY
from Review.models import Reviews
from Review.forms import ReviewForm
#from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#from django.db.models import Q
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from Cart.models import CART
import json
from Cart.context_processors import get_cart_items
# Create your views here.

def catItem(request,cat_slug):
    products = None
    categories = None
    if cat_slug is not None:
        # categories = get_object_or_404(CATEGORY,slug = cat_slug)
        categories = CATEGORY.objects.get(slug=cat_slug)
        print(f'subcate:{categories}')
        products= PRODUCTS.objects.filter(category=categories)
        #men_items = PRODUCTS.objects.filter(category__slug=men)
        productImg=IMAGE.objects.filter(product__in=products)
        
        # paginator = Paginator(products,3)
        # pageNumber = request.GET.get("page")
        # pageProduct = paginator.get_page(pageNumber)
        productCount = products.count()
        context = { 'products':products,
                    'productImg':productImg,
                    # 'colorattr':colorattr,
                    # 'sizeattr':sizeattr,
                    'productCount':productCount
                     }
    else:
        print(f'No category found for this link')
    return render(request,'Inventory/productCate1.html',context )

def menItem(request):
    menCat = CATEGORY.objects.filter(slug='men')
    menProducts = PRODUCTS.objects.filter(category=menCat)
    productImg=IMAGE.objects.filter(product__in=menProducts)
    context={
        'products':menProducts,
        'productImg':productImg
    }
    return render(request,'Inventory/productCate1.html')

# def FilterByColor(request,cate_slug,color_name):
#      products = PRODUCTS.objects.filter(category__slug=cate_slug)
#      colorproduct = COLORS.objects.filter(product__category__slug=cate_slug,name=color_name)
#      print(f'color:{colorproduct}')
#      #ChooseProduct = PRODUCTS.objects.filter(category__slug=cate_slug)
#      #return HttpRequest('hello')
#      return render(request,'Inventory/productCate1.html')


def productDetails(request,cate_slug,prod_slug):
        ChooseProduct = get_object_or_404(PRODUCTS,category__slug=cate_slug,slug=prod_slug)
        print(f'choseproduc:{ChooseProduct}')
        ProductImg = IMAGE.objects.get(product=ChooseProduct)
        price = PRICE.objects.get(product=ChooseProduct)
        stocks = STOCKS.objects.get(product=ChooseProduct)
        attributes = ATTRIBUTEVALUE.objects.all()
        releteImg = IMAGE.objects.all()
        reviews = Reviews.objects.filter(product=ChooseProduct)
        # cartProducts=0
        if request.user.is_authenticated:
            try:
                cartProducts =CART.objects.get(user=request.user,product=ChooseProduct)
                # print(f'items{cartProducts}')
            except ObjectDoesNotExist:
                cartProducts=None
        else:
            cartProducts=None
            
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
                'cartProducts':cartProducts,
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
                    return JsonResponse({'status':'Success','message':'Product increased','cartCount':get_cart_items(request),'prodQnty':productIncart.qty})
                except:
                    productIncart = CART.objects.create(user=request.user,product=ChooseProduct,qty=1)
                    return JsonResponse({'status':'Success','message':'Product added','cartCount':get_cart_items(request),'prodQnty':productIncart.qty})
            except:
                return JsonResponse({'status':'Failed','message':'This product is not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid request'})
    else:
        return JsonResponse({'status':'login_required','message':'You should login first'})

def RemoveProduct(request,cate_slug,prod_slug):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                ChooseProduct = PRODUCTS.objects.get(category__slug=cate_slug,slug=prod_slug)
                # check wether this product is already in cart
                try:
                    productIncart = CART.objects.get(user=request.user,product=ChooseProduct)
                    if productIncart.qty >1:
                        productIncart.qty -= 1
                        productIncart.save()
                    else:
                        productIncart.delete()
                        productIncart.qty =0
                    return JsonResponse({'status':'Success','message':'Product deleted','cartCount':get_cart_items(request),'prodQnty':productIncart.qty})
                except:
                    return JsonResponse({'status':'Success','message':'Your Cart is Empty','prodQnty':productIncart.qty})
            except:
                return JsonResponse({'status':'Failed','message':'Your product is not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid request'})
    else:
        return JsonResponse({'status':'login_required','message':'You should login first'})
    