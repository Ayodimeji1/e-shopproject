import stripe
from django.shortcuts import render

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from cart.forms import CheckoutForm
from eshopproject.settings import dev

from order.utilities import checkout
from .cart import Cart


# Create your views here.

def cart_detail(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            stripe.api_key = dev.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']

            try:
                charge = stripe.Charge.create(
                    amount=int(cart.get_total_cost() * 100),
                    currency='USD',
                    description='Purchase receipt',
                    source=stripe_token
                )

                full_name = form.cleaned_data['full_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']

                order = checkout(request, full_name, email, phone, address, zipcode,
                                 cart.get_total_cost())

                cart.clear()

                return redirect('success')
            except Exception:
                messages.error(request, 'There was something wrong with the payment')
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request, 'cart/cart.html', {'form': form, 'stripe_pub_key': dev.STRIPE_PUB_KEY})


def success(request):

    return render(request, 'cart/success.html')