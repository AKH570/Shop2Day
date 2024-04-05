from django.contrib import admin
from Accounts.models import User
from django.contrib.auth.admin import UserAdmin

# To non editable password field:
class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,CustomUserAdmin)
