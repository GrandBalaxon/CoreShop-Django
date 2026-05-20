from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "country", "phone_number")
    search_fields = ("username", "email", "phone_number")
    ordering = ("username", "date_joined")
