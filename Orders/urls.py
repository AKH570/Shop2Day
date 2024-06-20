from django.urls import path
from . import views

urlpatterns=[
    path('incart/checkout/neworder',views.newOrders,name='neworder'),
    path('orderconfirm/<str:orderno>',views.Orderconfirm,name='orderconfirm'),
]