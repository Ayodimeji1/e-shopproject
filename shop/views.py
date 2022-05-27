from django.shortcuts import render
from product.models import Category, Product

# Create your views here.


def index(request):
    category = Category.objects.all()
    products = Product.objects.all()[4:8]
    best_deals = Product.objects.filter(status="Sale")

    return render(request,'shop/index.html', {'category': category, 'products':  products, 'best_deals': best_deals})

