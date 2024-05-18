from django.shortcuts import render,redirect
from Cart.models import CART
from Inventory.models import PRICE
from Orders.forms import OrderForm
from Orders.models import Order
from Orders.utils import Order_number
# Create your views here.

def newOrders(request,subtotal=0):
    myCart = CART.objects.filter(user=request.user)
    cart_count = myCart.count()
    if cart_count == 0:
        return redirect('index')
    for i in myCart:
        value = PRICE.objects.get(product=i.product)
        subtotal += (i.qty * value.mrp)
    if request.method == 'POST':
        form=OrderForm(request.POST)
        print(f'form is{form}')
        if form.is_valid:
            order = Order()
            order.user = request.user
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone_no = form.cleaned_data['phone_no']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.country = form.cleaned_data['country']
            order.district = form.cleaned_data['district']
            order.billAmount = subtotal
            order.paymentMethod = request.POST['payment-method']
            order.save() # here the order id will be generated then pass it to oreder_number
            order.orderNo = Order_number(order.id) # here pk is id
            order.save()
            return redirect('order')
        else:
            print(form.errors)
   
        # context ={
        #     'myCart':myCart,
        #     'subtotal':subtotal,
            
        # }
    return render(request,'Orders/neworders.html')