from django.shortcuts import render
from .models import Product


def all_products(request):
    """A view that returns a list of all the products, search and sort queries"""

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/all_products.html', context)
