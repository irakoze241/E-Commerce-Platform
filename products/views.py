from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    """Home page — list all products with optional category filter."""
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category_slug = request.GET.get('category')
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    """Product detail page."""
    product = get_object_or_404(Product, pk=pk, available=True)
    related_products = Product.objects.filter(
        category=product.category, available=True
    ).exclude(pk=pk)[:4]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)
