from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "full_name", "is_staff", "is_active", "is_superuser")
    ordering = ("email",)
    search_fields = ("email",)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
