from catalog.models import Product
from django.shortcuts import get_object_or_404, render


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/product_list.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "catalog/product.html", context)
