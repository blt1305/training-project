from django.contrib import admin
from .models import Article

admin.site.register(Article)

from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)



