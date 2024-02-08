from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.UserAdmin):
    list_display = ["username", "email", "password"]
    list_filter = ["username", "email"]
