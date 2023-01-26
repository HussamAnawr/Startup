from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.




class UserAdmin(BaseUserAdmin):
    ordering = ['email', 'is_staff']
    exclude = ['username']
    list_display = ['email', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        (_('Basic Information'), {
            "fields": (
                'first_name', 'last_name'
            ),
        }),
        (_('Permission'), {
            "fields": (
                'is_superuser', 'is_staff', 'is_active'
            ),
        }),
        (_('Admin Permission'), {
            "fields": (
                'user_permissions',
            ),
        }),
        (_('Groups'), {
            "fields": (
                'groups',
            ),
        }),
        (_('Important dated'), {
            "fields": (
                'last_login', 'date_joined'
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        (_('Basic Information'), {
            "fields": (
                'first_name', 'last_name'
            ),
        }),
        (_('Permission'), {
            "fields": (
                'is_superuser', 'is_staff', 'is_active'
            ),
        }),
        (_('Admin Permission'), {
            "fields": (
                'user_permissions',
            ),
        }),
        (_('Groups'), {
            "fields": (
                'groups',
            ),
        }),

    )
    readonly_fields = ['last_login', 'date_joined']
    

admin.site.register(User, UserAdmin)