from django.contrib import admin

from .models import Payment, OrderItem

# Register your models here.

admin.site.register(Payment)
admin.site.register(OrderItem)