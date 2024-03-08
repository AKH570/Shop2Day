from django.urls import path
from Home import views

urlpatterns = [
    path('',views.home,name='index'),
    path('search/',views.search,name='search')
]