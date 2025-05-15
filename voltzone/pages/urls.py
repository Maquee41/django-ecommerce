from django.urls import path

from pages.views import about, homepage


app_name = "pages"

urlpatterns = [
    path("", homepage, name="home"),
    path("about/", about, name="about"),
]
