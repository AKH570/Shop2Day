from django.urls import path
from . import views

urlpatterns=[
    path('neworder/',views.newOrders,name='neworder'),
    path('orderconfirm/<str:orderno>',views.Orderconfirm,name='orderconfirm'),
]