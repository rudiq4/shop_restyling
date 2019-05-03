from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.html import format_html


def order_detail(obj):
    return format_html('<a href="{}">Переглянути</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_detail, 'size', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', ]
    list_filter = ['paid', 'created', 'updated']
    inLines = [OrderItemInLine]


admin.site.register(Order, OrderAdmin)
