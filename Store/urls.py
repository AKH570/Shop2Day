from django.urls import path
from Store import views
urlpatterns=[
    path('inventory',views.Inventory,name='store'),
]