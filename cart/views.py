from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .cart import Cart


def cart_detail(request):
    """Display the shopping cart."""
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    """Add a product to the cart or update quantity."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)

    quantity = int(request.POST.get('quantity', 1))
    update = request.POST.get('update', False)

    if quantity < 1:
        messages.error(request, 'Quantity must be at least 1.')
        return redirect('cart_detail')

    cart.add(product=product, quantity=quantity, update_quantity=bool(update))
    messages.success(request, f'"{product.name}" has been updated in your cart.')
    return redirect('cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Remove a product from the cart (POST only — CSRF protected)."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'"{product.name}" removed from cart.')
    return redirect('cart_detail')
