from django.contrib import admin
from apps.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'telegram_id', 'role')
