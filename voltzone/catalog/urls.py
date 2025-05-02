from django.urls import path, re_path

import catalog.views


urlpatterns = [
    path("", catalog.views.product_list, name="product-list"),
    path('category/<slug:category_slug>/', catalog.views.product_categories, name='product_list_by_category'),
    re_path(
        r"^(?P<product_id>\d+)/$",
        catalog.views.product_detail,
        name="product-detail",
    ),
]
