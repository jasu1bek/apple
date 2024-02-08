from django.contrib import admin
from .models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["name," "adress", "phone_number", "email"]
    list_filter = ["name", "adress"]