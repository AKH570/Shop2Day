
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('Accounts.urls')),
    path('',include('Home.urls')),
    path('',include('Inventory.urls')), 
    # path('',include('Store.urls')),
    path('',include('Cart.urls')),
    path('',include('Orders.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
