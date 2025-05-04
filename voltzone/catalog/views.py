import django.shortcuts

from catalog.models import Category, Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return django.shortcuts.render(
        request, "catalog/product_list.html", context
    )


def product_categories(request, category_slug):
    category = django.shortcuts.get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category).order_by("price")
    context = {
        "category": category,
        "products": products,
    }
    return django.shortcuts.render(
        request, "catalog/product_list.html", context
    )


def product_detail(request, product_id):
    product = django.shortcuts.get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return django.shortcuts.render(request, "catalog/product.html", context)
