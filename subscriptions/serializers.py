from rest_framework import serializers
from .models import SubscriptionPlan, UserSubscription


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = [
            'id', 'plan_name', 'price', 'duration_days', 'description',
            'includes_hd', 'max_streams', 'includes_offline',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    plan_name = serializers.CharField(source='plan.plan_name', read_only=True)

    class Meta:
        model = UserSubscription
        fields = [
            'id', 'user', 'plan', 'plan_name',
            'start_date', 'end_date', 'is_active', 'auto_renew',
            'created_at', 'updated_at',
        ]
        read_only_fields = [
            'id', 'user', 'plan_name', 'start_date',
            'created_at', 'updated_at',
        ]
