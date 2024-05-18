from django.urls import path
from . import views

urlpatterns=[
    path('order/',views.newOrders,name='order')
]