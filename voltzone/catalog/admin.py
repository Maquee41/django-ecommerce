from catalog.models import Category, Product
from django.contrib import admin
from django.utils.safestring import mark_safe


admin.site.register(Category)


@admin.register(Product)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" />')
