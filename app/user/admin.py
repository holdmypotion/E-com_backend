from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group

from user import models
from address.models import Address


class AddressInline(admin.StackedInline):
    model = Address


class UserAdmin(BaseUserAdmin):
    """
        User Admin model to structure the presentation
        of user attributes accordingly.
    """
    ordering = ['id']
    list_display = ['email', 'name']
    inlines = [
        AddressInline,
    ]
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.unregister(Group)
