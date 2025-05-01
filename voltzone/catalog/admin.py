from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from catalog.models import Category, Product


admin.site.register(Category)


@admin.register(Product)
class ItemAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img width=300 src="{obj.image.url}" />')
