from django.shortcuts import render, redirect
from .forms import *


def homeview(request, *args, **kwargs):
    return render(request, "main.html")


def Playfair_C(request, *args, **kwargs):
    from secretpy import Playfair

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Playfair().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Playfair().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Plaifair Cipher",
            },
        )


def Affine_c(request, *args, **kwargs):
    from secretpy import Affine

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Affine().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Affine Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Affine().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Affine Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Affine Cipher",
            },
        )


def ADFGVX_c(request, *args, **kwargs):
    from secretpy import ADFGVX

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(ADFGVX().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "ADFGVX Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(ADFGVX().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "ADFGVX Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "ADFGVX Cipher",
            },
        )


def ADFGX_c(request, *args, **kwargs):
    from secretpy import ADFGX

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(ADFGX().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "ADFGX Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(ADFGX().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "ADFGX Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "ADFGX Cipher",
            },
        )


def Autokey_c(request, *args, **kwargs):
    from secretpy import Autokey

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Autokey().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Autokey Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Autokey().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Autokey Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Autokey Cipher",
            },
        )


def Atbash_c(request, *args, **kwargs):
    from secretpy import Atbash

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Atbash().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Atbash Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Atbash().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Atbash Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Atbash Cipher",
            },
        )


def Bazeries_c(request, *args, **kwargs):
    from secretpy import Bazeries

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Bazeries().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Bazeries Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Bazeries().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Bazeries Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Bazeries Cipher",
            },
        )


def Beaufort_c(request, *args, **kwargs):
    from secretpy import Beaufort

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Beaufort().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Beaufort Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Beaufort().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Beaufort Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Beaufort Cipher",
            },
        )


def Bifid_c(request, *args, **kwargs):
    from secretpy import Bifid

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Bifid().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Bifid Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Bifid().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Bifid Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Bifid Cipher",
            },
        )


def Caesar_Progressive_c(request, *args, **kwargs):
    from secretpy import CaesarProgressive

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(
                CaesarProgressive().encrypt(plaintext, key)
            )
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "CaesarProgressive Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(
                CaesarProgressive().decrypt(plaintext, key)
            )

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "CaesarProgressive Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "CaesarProgressive Cipher",
            },
        )


def Caesar_c(request, *args, **kwargs):
    from secretpy import Caesar

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Caesar().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Caesar Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Caesar().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Caesar Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Caesar Cipher",
            },
        )


def Chaocipher_c(request, *args, **kwargs):
    from secretpy import Chao

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Chao().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Chao Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Chao().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Chao Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Chao Cipher",
            },
        )


def Columnar_Transposition_c(request, *args, **kwargs):
    from secretpy import ColumnarTransposition

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(
                ColumnarTransposition().encrypt(plaintext, key)
            )
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "ColumnarTransposition Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(
                ColumnarTransposition().decrypt(plaintext, key)
            )

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "ColumnarTransposition Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "ColumnarTransposition Cipher",
            },
        )


def Gronsfeld_c(request, *args, **kwargs):
    from secretpy import Gronsfeld

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        try:
            key = list(map(int, str(request.POST.get("key")).split()))
        except Exception as e:
            return render(
                request,
                "typeErr.html",
                {
                    "message": "Key Must Be Space Seperated Integer",
                    "backto": "Gronsfeld",
                },
            )
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Gronsfeld().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Gronsfeld Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Gronsfeld().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Gronsfeld Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Gronsfeld Cipher",
            },
        )


def Keyword_c(request, *args, **kwargs):
    from secretpy import Keyword

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Keyword().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Keyword Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Keyword().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Keyword Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Keyword Cipher",
            },
        )


def Myszkowski_Transposition_c(request, *args, **kwargs):
    from secretpy import MyszkowskiTransposition

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(
                MyszkowskiTransposition().encrypt(plaintext, key)
            )
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "MyszkowskiTransposition Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(
                MyszkowskiTransposition().decrypt(plaintext, key)
            )

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "MyszkowskiTransposition Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "MyszkowskiTransposition Cipher",
            },
        )


def Nihilist_c(request, *args, **kwargs):
    from secretpy import Nihilist

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Nihilist().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Nihilist Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Nihilist().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Nihilist Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Nihilist Cipher",
            },
        )


def Playfair_Two_c(request, *args, **kwargs):
    from secretpy import TwoSquare

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(TwoSquare().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Two Square Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(TwoSquare().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Two Square Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Plaifair Two Square Cipher",
            },
        )


def Playfair_Three_c(request, *args, **kwargs):
    from secretpy import ThreeSquare

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(
                ThreeSquare().encrypt(plaintext, key)
            )
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Three Square Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(
                ThreeSquare().decrypt(plaintext, key)
            )

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Three Square Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Plaifair Three Square Cipher",
            },
        )


def Playfair_Four_c(request, *args, **kwargs):
    from secretpy import FourSquare

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(FourSquare().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Four Square Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(FourSquare().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Plaifair Four Square Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Plaifair Four Square Cipher",
            },
        )


def Polybius_c(request, *args, **kwargs):
    from secretpy import Polybius

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Polybius().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Polybius Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Polybius().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Polybius Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Polybius Cipher",
            },
        )


def Porta_c(request, *args, **kwargs):
    from secretpy import Porta

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Porta().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Porta Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Porta().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Porta Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Porta Cipher",
            },
        )


def Rot5_c(request, *args, **kwargs):
    from secretpy import Rot5

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Rot5().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot5 Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Rot5().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot5 Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Rot5 Cipher",
            },
        )


def Rot13_c(request, *args, **kwargs):
    from secretpy import Rot13

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Rot13().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot13 Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Rot13().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot13 Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Rot13 Cipher",
            },
        )


def Rot18_c(request, *args, **kwargs):
    from secretpy import Rot18

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Rot18().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot18 Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Rot18().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot18 Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Rot18 Cipher",
            },
        )


def Rot47_c(request, *args, **kwargs):
    from secretpy import Rot47

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Rot47().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot47 Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Rot47().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Rot47 Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Rot47 Cipher",
            },
        )


def Simple_Substitution_c(request, *args, **kwargs):
    from secretpy import SimpleSubstitution

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(
                SimpleSubstitution().encrypt(plaintext, key)
            )
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "SimpleSubstitution Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(
                SimpleSubstitution().decrypt(plaintext, key)
            )

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "SimpleSubstitution Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "SimpleSubstitution Cipher",
            },
        )


def Trifid_c(request, *args, **kwargs):
    from secretpy import Trifid

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Trifid().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Trifid Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Trifid().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Trifid Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Trifid Cipher",
            },
        )


def Vic_c(request, *args, **kwargs):
    from secretpy import Vic

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = int(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Vic().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Vic Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Vic().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Vic Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Vic Cipher",
            },
        )


def Vigenere_c(request, *args, **kwargs):
    from secretpy import Vigenere

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        key = str(request.POST.get("key"))
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Vigenere().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Vigenere Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(Vigenere().decrypt(plaintext, key))

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Vigenere Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Vigenere Cipher",
            },
        )


def Zigzag_c(request, *args, **kwargs):
    from secretpy import Zigzag

    form_field = RawForms({})
    if request.method == "POST":
        plaintext = str(request.POST.get("plaintext"))
        try:
            key = int(request.POST.get("key"))
        except Exception as e:
            return render(
                request,
                "typeErr.html",
                {"message": "Key Must Be Integer", "backto": "Zigzag"},
            )
        if request.POST.get("type") == "Encryption":
            enc = "Your Encrypted text is: " + str(Zigzag().encrypt(plaintext, key))
            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": enc,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Zigzag Cipher",
                },
            )
        elif request.POST.get("type") == "Decryption":
            dec = "Your Decrypted Text is: " + str(
                Zigzag().decrypt(plaintext, int(key))
            )

            return render(
                request,
                "technique.html",
                {
                    "key_form_field": form_field["key"],
                    "plaintext_form_field": form_field["plaintext"],
                    "radio_field": form_field["type"],
                    "result_value": dec,
                    "key": "Your key:" + str(key),
                    "plaintext": "Your plaintext :" + str(plaintext),
                    "technique_name": "Zigzag Cipher",
                },
            )
    else:
        return render(
            request,
            "technique.html",
            {
                "key_form_field": form_field["key"],
                "plaintext_form_field": form_field["plaintext"],
                "radio_field": form_field["type"],
                "technique_name": "Zigzag Cipher",
            },
        )
