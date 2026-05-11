from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'price', 'duration_days', 'includes_hd', 'max_streams')
    list_filter = ('plan_name', 'includes_hd', 'includes_offline')
    search_fields = ('plan_name',)


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'is_active', 'start_date', 'end_date')
    list_filter = ('plan', 'is_active', 'auto_renew')
    search_fields = ('user__email', 'plan__plan_name')
    raw_id_fields = ('user', 'plan')
