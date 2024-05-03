from django.contrib import admin
from .models import CART

# Register your models here.
@admin.register(CART)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['user','product','qty','created_at']
    list_filter=('user','product',)