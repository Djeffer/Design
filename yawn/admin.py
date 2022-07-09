from django.contrib import admin
from .models import StatusYawn, Order, CommentsYawn


class Comment(admin.StackedInline):
    model = CommentsYawn
    fields = ("comment_dt", "comment_text")
    readonly_fields = ("comment_dt",)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt', 'order_city')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt', 'order_city')
    readonly_fields = ('id', 'order_dt',)
    list_per_page = 10
    inlines = [Comment]


admin.site.register(StatusYawn)
admin.site.register(Order, OrderAdm)
admin.site.register(CommentsYawn)
