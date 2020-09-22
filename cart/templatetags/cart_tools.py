from django import template

register = template.Library()


@register.filter(name='subtotal_calc')
def subtotal_calc(price, quantity):
    return price * quantity
