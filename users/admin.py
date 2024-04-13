from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'id_telegram', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', )
    list_filter = ('email', 'id_telegram', 'is_staff', 'is_active', 'is_superuser',)
    search_fields = ('first_name', 'last_name', 'email',)
