from django.contrib import admin
from django.contrib import messages

from . import models


class OrderAdmin(admin.ModelAdmin):
    """Extra functionalities on the admin interface"""
    search_fields = ['user', 'product']
    list_display = ['id', 'user', 'product', 'quantity', 'done']
    list_editable = ['done']
    list_filter = ['user', 'done', 'product']
    readonly_fields = ['timestamp', 'updated']

    def mark_done(modeladmin, request, queryset):
        queryset.update(done=True)
        messages.success(request, "Selected Record(s) Marked as Done!!")

    def mark_undone(modeladmin, request, queryset):
        queryset.update(done=False)
        messages.success(request, "Selected Record(s) Marked as Undone!!")

    admin.site.add_action(mark_done, "Mark done")
    admin.site.add_action(mark_undone, "Mark undone")

    class Meta:
        model = models.Order


admin.site.register(models.Order, OrderAdmin)
