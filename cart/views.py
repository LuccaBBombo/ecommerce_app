from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """A view to render the cart content page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds chosen quantity of a chosen item to the shopping cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Updates item quantity in the cart for the selected item"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop[item_id]

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_item_cart(request, item_id):
    """ Deletes the selected item in the cart"""

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
