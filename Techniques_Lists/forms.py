from django import forms

types = [
    ("Encryption", "Encryption"),
    ("Decryption", "Decryption"),
]


class RawForms(forms.Form):
    type = forms.CharField(widget=forms.RadioSelect(choices=types),label='')
    plaintext = forms.CharField(strip=True)
    key = forms.CharField(strip=True)
    