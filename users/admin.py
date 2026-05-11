from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'email', 'phone_number',
        'subscription_status', 'is_staff', 'is_active',
    )
    list_filter = ('subscription_status', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('email',)
    fieldsets = UserAdmin.fieldsets + (
        ('Subscription details', {'fields': ('subscription_status', 'subscription_end_date')}),
        ('Profile details', {'fields': ('phone_number', 'bio', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Subscription details', {'fields': ('subscription_status', 'subscription_end_date')}),
    )
