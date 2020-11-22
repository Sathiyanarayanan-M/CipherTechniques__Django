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
    path("Affine", views.Affine_c),
    path("Playfair", views.Playfair_C),
    path("ADFGX" or "/ADFGX/", views.ADFGX_c, name="adfgx"),
    path("ADFGVX", views.ADFGVX_c),
    path("Atbash", views.Atbash_c),
    path("Autokey", views.Autokey_c),
    path("Bazeries", views.Bazeries_c),
    path("Beaufort", views.Beaufort_c),
    path("Bifid", views.Bifid_c),
    path("Caesar_Progressive", views.Caesar_Progressive_c),
    path("Caesar", views.Caesar_c),
    path("Chaocipher", views.Chaocipher_c),
    path("Columnar_Transposition", views.Columnar_Transposition_c),
    path("Gronsfeld", views.Gronsfeld_c),
    path("Keyword", views.Keyword_c),
    path("Myszkowski_Transposition", views.Myszkowski_Transposition_c),
    path("Nihilist", views.Nihilist_c),
    path("Playfair_Two", views.Playfair_Two_c),
    path("Playfair_Three", views.Playfair_Three_c),
    path("Playfair_Four", views.Playfair_Four_c),
    path("Polybius", views.Polybius_c),
    path("Porta", views.Porta_c),
    path("Rot5", views.Rot5_c),
    path("Rot13", views.Rot13_c),
    path("Rot18", views.Rot18_c),
    path("Rot47", views.Rot47_c),
    path("Simple_Substitution", views.Simple_Substitution_c),
    path("Trifid", views.Trifid_c),
    path("Vic", views.Vic_c),
    path("Vigenere", views.Vigenere_c),
    path("Zigzag", views.Zigzag_c),
]
