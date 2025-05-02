from django.urls import path

from pages.views import about, homepage


urlpatterns = [
    path("", homepage, name="homepage"),
    path("about/", about, name="about"),
]
