from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = (
    [
        path("", include("pages.urls")),
        path("catalog/", include("catalog.urls")),
        path("admin/", admin.site.urls),
        path("summernote/", include("django_summernote.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
