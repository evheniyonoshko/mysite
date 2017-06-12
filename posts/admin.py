# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from posts.forms import UserAdminForm
from posts.models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    ordering = ('registered',)
    list_filter = ['is_active']

    list_display = (
        'email', 'first_name', 'last_name', 'is_superuser', 'is_active', 'is_staff'
    )

    fieldsets = (
        ('Info', {
            'fields': ('email', 'first_name', 'last_name','birthday', 'country', 'city')
        }),
        ('Permissions', {
            'fields': ('is_superuser','is_staff', 'is_active')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username',
                       'first_name', 'last_name', 'birthday', 'country', 'city')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_active')
        }),
    )

    class Media:
        css = {
        }
        js = (
        )

admin.site.register(User, UserAdmin)
