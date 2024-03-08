from django.contrib import admin
from . models import CATEGORY
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title',)}
    list_display = ['title','slug','description','cat_image']
admin.site.register(CATEGORY,CategoryAdmin)