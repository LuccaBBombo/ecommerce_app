from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Allow admin to see a list of editable line items instead of needing to access the item interface"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total', 'grand_total',)
    fields = ('order_number', 'full_name', 'email', 'phone_number',
              'country', 'postcode', 'city', 'street_address1', 'street_address2',
              'county', 'date', 'delivery_cost', 'order_total', 'grand_total',)

    list_display_fields = ('order_number', 'full_name',
                           'email', 'order_total', 'delivery_cost', 'grand_total',)
    order = ('-date',)


admin.site.register(Order, OrderAdmin)
