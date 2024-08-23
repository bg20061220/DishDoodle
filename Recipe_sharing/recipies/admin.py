

from django.contrib import admin
from django.contrib.auth.models import User

# Define a new UserAdmin class
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active' , 'id')
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Optional: Adds a search bar

# Unregister the default User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

