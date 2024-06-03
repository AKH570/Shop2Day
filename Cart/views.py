from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE
from Cart.models import CART
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from Cart.context_processors import get_cart_items
from Orders.forms import OrderForm
from Accounts.models import User

# Create your views here.
@login_required(login_url='login')
def myCart(request,subtotal=0,quantity=0,myCart=None):
    myCart = CART.objects.filter(user=request.user)
    for i in myCart:
        value = PRICE.objects.get(product=i.product)
        subtotal += (i.qty * value.mrp)
        quantity = i.qty
        print(f'quanty:{quantity}')
    context ={
        'myCart':myCart,
        # 'subtotal':subtotal,
        # 'quantity':quantity,
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

@login_required(login_url='login')
def checkout(request,Grand_Total=0,total=0,delivery_charge=0):
    myCart = CART.objects.filter(user=request.user)
    cart_count = myCart.count()
    if cart_count == 0:
        return redirect('index')
    # to prepopulate checkout form
    default_user_info = {
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
        'phone_no':request.user.phone_no,
    }
    form = OrderForm(initial=default_user_info) #it pick the user data from user
 
    for i in myCart:
        total += (i.qty * i.product.product_price)
    delivery_charge = 100
    Grand_Total = total+delivery_charge
    context ={
        'myCart':myCart,
        'total':total,
        'Grand_Total':Grand_Total,
        'delivery_charge':delivery_charge,
        'form':form,
    }
    return render(request,'Cart/checkout.html',context)
