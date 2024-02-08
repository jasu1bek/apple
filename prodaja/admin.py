from django.contrib import admin
from .models import Prodaja 


@admin.register(Prodaja)
class ProdajaAdmin(adminProdajaAdmin):
    list_display = ["product_name", "username", "total_price"]
    list_filter = ["product_name", "total_price"]