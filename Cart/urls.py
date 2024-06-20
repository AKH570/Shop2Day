from django.urls import path
from . import views

urlpatterns = [
    path('incart',views.myCart,name='incart'),
    path('del_cart/<int:cartId>',views.deleteCart,name='del_cart'),
    path('incart/checkout',views.checkout,name='mycheckout')
]