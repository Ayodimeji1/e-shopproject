from django import forms
from django.forms.fields import CharField


class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    zipcode = forms.IntegerField()
    stripe_token = forms.CharField(max_length=255)