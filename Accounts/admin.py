from django.contrib import admin
from Accounts.models import User
from django.contrib.auth.admin import UserAdmin

# To non editable password field:
class CustomUserAdmin(UserAdmin):
    list_display=['username','first_name','last_name','email','phone_no','role','checkbox',
    'is_active','is_admin','is_staff','is_superuser']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(User,CustomUserAdmin)
