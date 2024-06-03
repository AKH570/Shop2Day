from django.contrib import admin
from Orders.models import Order,OrderedItem

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=['orderNo','name','email','phone_no',
    'address','district','country','user','billAmount','status','is_ordered','created_at']
    list_filter = ['status','is_ordered']
    search_fields = ['orderNo','phone_no']
    list_per_page = 20
admin.site.register(Order,OrderAdmin)

class OrderedItemAdmin(admin.ModelAdmin):
    list_display=['order','user','productItem','quantity','price','amount','orderedSuccess','created_at']
    list_filter=['user','orderedSuccess']
admin.site.register(OrderedItem,OrderedItemAdmin)
