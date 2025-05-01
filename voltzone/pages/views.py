from django.shortcuts import get_object_or_404, render

from pages.models import HomePage


def homepage(request):
    homepage_info = get_object_or_404(HomePage, pk=1)
    context = {"homepage_info": homepage_info}
    return render(request, "pages/home.html", context)
