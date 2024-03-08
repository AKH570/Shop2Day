from django.contrib import admin
# Register your models here.
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass
