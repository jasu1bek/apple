from django.contrib import admin
from .models import Product 

@admin.register(Product)
class ProductAdmin(admin.ProductAdmin):
    list_display = ["name", "provider", "category", "brand", "price"]
    list_filter = ["name", "brand", "price"]
