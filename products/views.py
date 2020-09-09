from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """A view that returns a list of all the products, search and sort queries"""

    products = Product.objects.all()
    query = None

    """Query to filter objects by name or by description"""
    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "The item you searched was not found")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/all_products.html', context)


def product_info(request, product_id):
    """A view that returns a detailed page of the selected product by targeting its ID"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_info.html', context)
