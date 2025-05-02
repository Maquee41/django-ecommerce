from django.shortcuts import render


def homepage(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")
