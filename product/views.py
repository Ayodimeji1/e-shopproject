from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, Category
from django.db.models import Q

from cart.cart import Cart
from .forms import AddToCartForm

# Create your views here


def product(request, category_slug, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, "added to cart")

            return redirect('product', category_slug=category_slug, product_slug=product_slug)

    else:
        form = AddToCartForm()

    return render(request, 'product/product.html', {'form': form, 'product': product })


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})
