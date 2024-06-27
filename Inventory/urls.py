from django.urls import path
from Inventory import views

urlpatterns = [
    path('<slug:cat_slug>/',views.catItem,name='cat_item'),
    path('men_item/',views.menItem,name='men_item'),    
    path('<slug:cate_slug>/<slug:prod_slug>/',views.productDetails,name='productDetails'),
    path('my_reviews/<slug:cate_slug>/<slug:prod_slug>/',views.UserReviews,name='my_reviews'),
    path('cart/<slug:cate_slug>/<slug:prod_slug>/',views.AddProduct,name='add_prod'),
    path('removeprod/<slug:cate_slug>/<slug:prod_slug>/',views.RemoveProduct,name='removeprod'),
    
]

