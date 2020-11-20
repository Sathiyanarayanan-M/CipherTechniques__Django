from django.shortcuts import render

# Create your views here.
def homeview(request, *args, **kwargs):
    return render(request, "main.html", {})

def Playfair(request, *args, **kwargs):
    return render(request, "Playfair.html", {})

def Affine(request, *args, **kwargs):
    return render(request, "Affine.html", {})

def ADFGVX(request, *args, **kwargs):
    return render(request, "ADFGVX.html", {})

def ADFGX(request, *args, **kwargs):
    return render(request, "ADFGX.html", {})

def Autokey(request, *args, **kwargs):
    return render(request, "Autokey.html", {})

def Atbash(request, *args, **kwargs):
    return render(request, "Atbash.html", {})

def Bazeries(request, *args, **kwargs):
    return render(request, "Bazeries.html", {})

def Beaufort(request, *args, **kwargs):
    return render(request, "Beaufort.html", {})

def Bifid(request, *args, **kwargs):
    return render(request, "Bifid.html", {})

def Caesar_Progressive(request, *args, **kwargs):
    return render(request, "Caesar_Progressive.html", {})

def Caesar(request, *args, **kwargs):
    return render(request, "Caesar.html", {})

def Chaocipher(request, *args, **kwargs):
    return render(request, "Chaocipher.html", {})

def Columnar_Transposition(request, *args, **kwargs):
    return render(request, "Columnar_Transposition.html", {})

def Gronsfeld(request, *args, **kwargs):
    return render(request, "Gronsfeld.html", {})

def Keyword(request, *args, **kwargs):
    return render(request, "Keyword.html", {})

def Myszkowski_Transposition(request, *args, **kwargs):
    return render(request, "Myszkowski_Transposition.html", {})

def Nihilist(request, *args, **kwargs):
    return render(request, "Nihilist.html", {})

def Playfair_Two(request, *args, **kwargs):
    return render(request, "Playfair_Two.html", {})

def Playfair_Three(request, *args, **kwargs):
    return render(request, "Playfair_Three.html", {})

def Playfair_Four(request, *args, **kwargs):
    return render(request, "Playfair_Four.html", {})

def Polybius(request, *args, **kwargs):
    return render(request, "Polybius.html", {})

def Porta(request, *args, **kwargs):
    return render(request, "Porta.html", {})

def Rot5(request, *args, **kwargs):
    return render(request, "Rot5.html", {})

def Rot13(request, *args, **kwargs):
    return render(request, "Rot13.html", {})


def Rot18(request, *args, **kwargs):
    return render(request, "Rot18.html", {})

def Rot47(request, *args, **kwargs):
    return render(request, "Rot47.html", {})

def Simple_Substitution(request, *args, **kwargs):
    return render(request, "Simple_Substitution.html", {})

def Trifid(request, *args, **kwargs):
    return render(request, "Trifid.html", {})

def Vic(request, *args, **kwargs):
    return render(request, "Vic.html", {})

def Vigenere(request, *args, **kwargs):
    return render(request, "Vigenere.html", {})

def Zigzag(request, *args, **kwargs):
    return render(request, "Zigzag.html", {})
