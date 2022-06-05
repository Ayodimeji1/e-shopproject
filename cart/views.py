from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from payment import forms
from payment.models import Payment
from payment.forms import CheckoutForm
from eshopproject.settings import dev

from payment.utilities import checkout
from .cart import Cart


# Create your views here.

def cart_detail(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request, 'cart/cart.html')




