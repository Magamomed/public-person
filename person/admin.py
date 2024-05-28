from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PublicPerson

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'is_approved']
    list_filter = ['is_approved']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_approved',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_approved',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PublicPerson)
