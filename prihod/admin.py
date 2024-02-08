from django.contrib import admin
from .models import Prihod 


@admin.register(Prihod)
class PrihodAdmin(admin.PrihodAdmin):
    list_display = ["provider_name", "username", "price"]
    list_filter = ["provider_name", "price"]