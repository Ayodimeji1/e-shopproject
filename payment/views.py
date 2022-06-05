from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from eshopproject.settings import dev
from .forms import CheckoutForm

from .models import Payment
# Create your views here


def initiate_payment(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    if request.method == 'POST':
        payment_form = CheckoutForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()

            cart.clear()

            return render(request, 'payment/make_payment.html',
                          {'payment': payment, 'paystack_public_key': dev.PAYSTACK_PUBLIC_KEY})

    else:
        payment_form = CheckoutForm()

    return render(request, 'payment/initiate_payment.html', {'payment_form': payment_form})


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'Verification Failed')
    return redirect('index')
