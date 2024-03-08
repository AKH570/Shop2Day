from django.contrib import admin
from . models import (PRODUCTS,ATTRIBUTES,BRAND,
                      ATTRIBUTEVALUE,STOCKS,IMAGE,PRICE,
                      SUBCATEGORY)
from Category.models import CATEGORY
# Register your models here.

# @admin.register(PRODUCT_CATEGORY)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id','name','slug','category','is_active']
#     prepopulated_fields = {'slug':('name',)}
#     list_editable = ('is_active',)
#     list_filter=('category',)
#admin.site.register(PRODUCTS,ProductAdmin)
# @admin.register(ATTRIBUTEVALUE)
# class AttributevalueAdmin(admin.ModelAdmin):
    #list_display = ['id','values','valueName','attribute']
    #ordering = ('id',)
# class AttributeValueInline(admin.TabularInline):
#     model = ATTRIBUTEVALUE
#@admin.register(ATTRIBUTES)
#class AttributeAdmin(admin.ModelAdmin):
    #inlines = [AttributeValueInline,]
    #list_display = ['name','description']

#Brand
@admin.register(BRAND)
class BrandAdmin(admin.ModelAdmin):
    pass

#Image
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','url','text','product',]
    list_filter = ('product',)
    ordering = ('id',)
admin.site.register(IMAGE,ImageAdmin)

#ADMIN FOR PRODUCT
class PriceInline(admin.TabularInline):
    model = PRICE
    extra = 1
class StockInline(admin.TabularInline):
    model = STOCKS
class ImageInline(admin.TabularInline):
    model = IMAGE
    extra = 1
@admin.register(PRODUCTS)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInline,StockInline,ImageInline]
    list_display=['id','name','slug','barcode','category',
                    'brandname','Owner','in_stocks',
                    'is_active','is_discount','create_date']
    search_fields=('name','subcategory__name',)
    prepopulated_fields ={'slug':('name',)}
    list_filter=('category',)
    exclude = ('attributevalue',)
    list_editable = ('in_stocks','is_active','is_discount',)
    ordering = ('id',)

@admin.register(PRICE)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['product','saleprice','storeprice','discount_percentage','mrp']

@admin.register(STOCKS)
class StocksAdmin(admin.ModelAdmin):
    list_display  =['id','quantity','unit','stocks_qty','product','last_checked',]
    list_filter=('product',)

@admin.register(SUBCATEGORY)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','is_active']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ('is_active',)
    list_filter=('category',)
#admin.site.register(PRODUCTS,ProductAdmin)