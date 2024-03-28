from django.urls import path
from Cart import views

urlpatterns = [
    path('cart/',views.Cart,name='cart'),
    path('cart/<int:product_id>/',views.AddToProduct,name='add_prod'),
    # path('get_data/',views.IncreaseCart,name='getdata'),
]