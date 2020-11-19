from django.shortcuts import render

# Create your views here.
def homeview(request, *args, **kwargs):
    return render(request, "main.html", {})


def playfair(request, *args, **kwargs):
    return render(request, "playfair.html", {})


def affine(request, *args, **kwargs):
    return render(request, "Affine.html", {})
