from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    """Extra functionalities on the admin interface"""
    search_fields = ['title', 'description', 'section']
    list_display = ['title', 'section', 'active', 'update']
    list_editable = ['active']
    list_filter = ['section', 'active']
    readonly_fields = ['timestamp', 'update']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = models.Product


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Section)
