from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register the User model with the custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

