from django.shortcuts import render,redirect,HttpResponse
from Cart.models import CART
from Inventory.models import PRICE,PRODUCTS,STOCKS
from Orders.forms import OrderForm
from Orders.models import Order,OrderedItem
from Orders.utils import Order_number
# Create your views here.

def newOrders(request,total=0,delivery_charge=0,Grand_Total=0):
    myCart = CART.objects.filter(user=request.user)
#    if cart is zero then system back to index page
    cart_count = myCart.count()
    if cart_count == 0:
        return redirect('index')

    for i in myCart:
        total += (i.qty * i.product.product_price)
    delivery_charge = 100
    Grand_Total = total+delivery_charge

    if request.method == 'POST':
        form=OrderForm(request.POST)
        # print(form)
        if form.is_valid():
            order = Order()
            order.user = request.user
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone_no = form.cleaned_data['phone_no']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.country = form.cleaned_data['country']
            order.district = form.cleaned_data['district']
            order.billAmount = Grand_Total
            order.paymentMethod = request.POST['payment-method']
            order.save()
            order_number= Order_number() + str(order.id) # here the order id will be generated then pass it to oreder_number
            order.orderNo = order_number # here pk is id
            order.save()
            # return redirect('order')
            neworder = Order.objects.get(user=request.user,orderNo=order_number)
            # print(f'Order_No: {neworder}')
            context ={
                'order':order,
                'myCart':myCart,
                'total':total,
                'delivery_charge':delivery_charge,
                'Grand_Total':Grand_Total,    
            }
            return render(request,'Orders/neworders.html',context)
        else:
            print(form.errors)
    return render(request,'Orders/neworders.html',)

def Orderconfirm(request,orderno):
    # return HttpResponse(orderno)
    try:
        neworder = Order.objects.get(user=request.user,is_ordered=False,orderNo=orderno)
        neworder.is_ordered = True
        neworder.save()

        myCart = CART.objects.filter(user=request.user)
        #to store data in Orderconfirm table
        for item in myCart:
            order_item= OrderedItem() # created the order_item orbject of OrderedItem model
            order_item.order_id=neworder.id # foreign key
            order_item.user_id=request.user.id # foreign key
            order_item.quantity = item.qty
            order_item.productItem_id = item.product_id # foreign key
            order_item.price = item.product.product_price
            order_item.amount=0
            order_item.orderedSuccess=True
            order_item.save()
        # reduce quantity of product from stock 
            stocks = STOCKS.objects.get(product=PRODUCTS.objects.get(id=item.product_id))
            stocks.quantity -= item.qty
            stocks.save()
        # clear the cart
        # CART.objects.filter(user=request.user).delete()
        # send order no and details in html page:
        ordereditem = OrderedItem.objects.filter(order=neworder)
        subtotal = 0
        total = 0
        for item in ordereditem:
            subtotal += (item.price*item.quantity)
        totat= subtotal+100
        context={
            'neworder':neworder,
            'ordereditem':ordereditem,
            'subtotal':subtotal,
            'totat':totat
        }
        return render(request,'Orders/confirmorder.html',context)
    except:
        neworder = Order.objects.get(user=request.user,is_ordered=True,orderNo=orderno)
        ordereditem = OrderedItem.objects.filter(order=neworder,orderedSuccess=True)
        subtotal = 0
        total = 0
        for item in ordereditem:
            subtotal += (item.price*item.quantity)
        total= subtotal+100
        context={
            'neworder':neworder,
            'ordereditem':ordereditem,
            'subtotal':subtotal,
            'total':total
        }
        return render(request,'Orders/confirmorder.html',context)