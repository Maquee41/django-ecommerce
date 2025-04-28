import catalog.views
from django.urls import path, re_path


urlpatterns = [
    path("", catalog.views.product_list, name="product-list"),
    re_path(
        r"^(?P<product_id>\d+)/$",
        catalog.views.product_detail,
        name="product-detail",
    ),
]
