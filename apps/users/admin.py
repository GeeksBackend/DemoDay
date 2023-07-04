from django.contrib import admin

from apps.users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined')
    search_fields = ('username', 'date_joined')