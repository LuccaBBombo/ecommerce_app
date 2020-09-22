from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse('products'))

    form_order = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form_order': form_order,
    }

    return render(request, template, context)
