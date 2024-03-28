from django.contrib import admin
from . models import (PRODUCTS,ATTRIBUTES,BRAND,
                      ATTRIBUTEVALUE,STOCKS,IMAGE,PRICE,
                      SUBCATEGORY)
from Category.models import CATEGORY
# Register your models here.
@admin.register(SUBCATEGORY)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','is_active']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ('is_active',)
    list_filter=('category',)

#Brand
@admin.register(BRAND)
class BrandAdmin(admin.ModelAdmin):
    pass

#ADMIN FOR PRODUCT
class StockInline(admin.TabularInline):
    model = STOCKS
    extra = 1
    classes=('collapse',)
# class PriceInline(admin.TabularInline):
#     model = PRICE.stock
#     extra = 1
class ImageInline(admin.TabularInline):
    model = IMAGE
    extra = 1
@admin.register(PRODUCTS)
class ProductAdmin(admin.ModelAdmin):
    inlines = [StockInline,ImageInline]
    list_display=['id','name','slug','barcode','category','subcategory',
                    'brandname','Owner','in_stocks',
                    'is_active','is_discount','create_date']
    search_fields=('name','subcategory__name',)
    prepopulated_fields ={'slug':('name',)}
    list_filter=('category',)
    exclude = ('attributevalue',)
    list_editable = ('in_stocks','is_active','is_discount',)
    ordering = ('id',)

class PriceInline(admin.TabularInline):
    model = PRICE
    extra = 1
@admin.register(STOCKS)
class StocksAdmin(admin.ModelAdmin):
    inlines=[PriceInline]
    list_display  =['id','product','quantity','unit','stocks_qty','last_checked',]
    list_filter=('product',)
    ordering = ('id',)
#Price
@admin.register(PRICE)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['id','stock','product','saleprice','storeprice','discount_percentage','total_store_price','mrp']
    ordering = ('id',)
#Image
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','url','text','product',]
    list_filter = ('product',)
    ordering = ('id',)
admin.site.register(IMAGE,ImageAdmin)


#admin.site.register(PRODUCTS,ProductAdmin)