from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import DesignSlid


class DesignAdmin(admin.ModelAdmin):
    list_display = ('design_title', 'design_id', 'design_css', 'get_img',)
    list_editable = ('design_css',)
    fields = ('get_img', 'design_title', 'design_css')
    readonly_fields = ('get_img',)
    list_per_page = 10

    def get_img(self, obj):
        if obj.design_img:
            return mark_safe(f"<img src='{obj.design_img.url}' width='100'>")
        else:
            return "Нет изображения"

    get_img.short_description = 'Миниатюра'


admin.site.register(DesignSlid, DesignAdmin)

