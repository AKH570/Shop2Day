from django.urls import path
from Cart import views

urlpatterns = [
    path('cart/',views.myCart,name='cart'),
    path('del_cart/<int:cartId>',views.deleteCart,name='del_cart')
]