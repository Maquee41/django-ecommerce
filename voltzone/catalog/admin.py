from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from catalog.models import Category, Product


admin.site.register(Category)


@admin.register(Product)
class ItemAdmin(SummernoteModelAdmin):
    list_display = (
        "name",
        "preview",
        "price",
        "count",
    )
    list_filter = ("category",)
    readonly_fields = ("preview",)
    summernote_fields = ("description",)

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img width=250 src="{obj.image.url}" />')

    preview.short_description = "превью"
