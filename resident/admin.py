from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, House


# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['first_name', 'last_name', 'email','username','phone']

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name", "email", "phone"),
            },
        ),
    )


    @admin.register(House)
    class HouseAdmin(admin.ModelAdmin):
        list_display = ['house_number', 'address']