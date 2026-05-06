from .cart import Cart


def cart_context(request):
    """Make cart available across all templates."""
    return {'cart': Cart(request)}
