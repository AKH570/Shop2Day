from django.contrib import admin
from Orders.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=['orderNo','name','email','phone_no','address','district','country','user']
admin.site.register(Order,OrderAdmin)