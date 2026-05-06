from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout(request):
    """Checkout page — display form and handle order placement."""
    cart = Cart(request)

    if cart.is_empty():
        messages.warning(request, 'Your cart is empty. Add some products first!')
        return redirect('product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create the Order
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                total_price=cart.get_total_price(),
            )

            # Create OrderItems from cart
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    product_name=item['name'],
                    quantity=item['quantity'],
                    price=item['price'],
                )
                # Deduct stock
                product = item['product']
                product.stock -= item['quantity']
                if product.stock < 0:
                    product.stock = 0
                product.save()

            # Clear cart
            cart.clear()
            messages.success(request, 'Order placed successfully! Thank you.')
            return redirect('order_confirm', order_id=order.id)
    else:
        # Pre-fill name if user has first/last name
        initial = {}
        if request.user.get_full_name():
            initial['full_name'] = request.user.get_full_name()
        form = CheckoutForm(initial=initial)

    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def order_confirm(request, order_id):
    """Order confirmation page."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_confirm.html', {'order': order})


@login_required
def order_history(request):
    """List all orders for the logged-in user."""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Detail view for a single order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
