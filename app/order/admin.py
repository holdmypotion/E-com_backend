from django.contrib import admin
from . import models


class OrderAdmin(admin.ModelAdmin):
    """Extra functionalities on the admin interface"""
    search_fields = ['user', 'product']
    list_display = ['order_id', 'user', 'product', 'quantity', 'done']
    list_editable = ['done']
    list_filter = ['user', 'done', 'product']
    readonly_fields = ['timestamp', 'updated']

    class Meta:
        model = models.Order


admin.site.register(models.Order, OrderAdmin)
