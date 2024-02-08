from django.contrib import admin
from .models import Category 


@admin.register(Category)
class CategoryAdmin(admin.CategoryAdmin):
    list_display = ["category_name"] 