from django.urls import path, re_path

import catalog.views


app_name = "catalog"

urlpatterns = [
    path("", catalog.views.product_list, name="list"),
    path(
        "category/<slug:category_slug>/",
        catalog.views.product_categories,
        name="list-category",
    ),
    re_path(
        r"^(?P<product_id>\d+)/$",
        catalog.views.product_detail,
        name="detail",
    ),
]
