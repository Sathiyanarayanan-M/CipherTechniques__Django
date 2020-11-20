"""Cipher_Techniques URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Techniques_Lists import views

urlpatterns = [
    path("", views.homeview),
    path("home" or "Home", views.homeview),
    path("Affine", views.Affine),
    path("Playfair", views.Playfair),
    path("ADFGX", views.ADFGX),
    path("ADFGVX", views.ADFGVX),
    path("Atbash", views.Atbash),
    path("Autokey", views.Autokey),
    path("Bazeries", views.Bazeries),
    path("Beaufort", views.Beaufort),
    path("Bifid", views.Bifid),
    path("Caesar_Progressive", views.Caesar_Progressive),
    path("Caesar", views.Caesar),
    path("Chaocipher", views.Chaocipher),
    path("Columnar_Transposition", views.Columnar_Transposition),
    path("Gronsfeld", views.Gronsfeld),
    path("Keyword", views.Keyword),
    path("Myszkowski_Transposition", views.Myszkowski_Transposition),
    path("Nihilist", views.Nihilist),
    path("Playfair_Two", views.Playfair_Two),
    path("Playfair_Three", views.Playfair_Three),
    path("Playfair_Four", views.Playfair_Four),
    path("Polybius", views.Polybius),
    path("Porta", views.Porta),
    path("Rot5", views.Rot5),
    path("Rot13", views.Rot13),
    path("Rot18", views.Rot18),
    path("Rot47", views.Rot47),
    path("Simple_Substitution", views.Simple_Substitution),
    path("Trifid", views.Trifid),
    path("Vic", views.Vic),
    path("Vigenere", views.Vigenere),
    path("Zigzag", views.Zigzag),
]
