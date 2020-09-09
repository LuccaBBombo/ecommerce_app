from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """A view that returns a list of all the products, search and sort queries"""

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/all_products.html', context)


def product_info(request, product_id):
    """A view that returns a detailed page of the selected product by targeting its ID"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_info.html', context)
