from django.urls import path
from Cart import views

urlpatterns = [
    path('cart/',views.myCart,name='cart'),
]