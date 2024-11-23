# Django 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Show list of users
    list_display = ("email", "username", "is_staff", "is_active")
    
    # Filte list of users
    list_filter = ("email", "username", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (                
                "email",
                "username",
                "password1", 
                "password2",
                "is_staff",
                "is_active",
                "groups",
                "user_permissions",
            )
        }),
    )

    search_fields = ("email", "username",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
