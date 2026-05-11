from django.db import models
from users.models import CustomUser


class SubscriptionPlan(models.Model):
    """Subscription plans available"""
    
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('premium', 'Premium'),
    ]
    
    plan_name = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        unique=True
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField(help_text='Duration in days')
    description = models.TextField(blank=True)
    
    # Features
    includes_hd = models.BooleanField(default=False)
    max_streams = models.IntegerField(default=1)
    includes_offline = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return f"{self.plan_name} - KSH {self.price}"


class UserSubscription(models.Model):
    """User subscription tracking"""
    
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_subscription'
    )
    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.SET_NULL,
        null=True,
        related_name='subscriptions'
    )
    
    # Subscription period
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    # Auto-renewal
    auto_renew = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.user.email} - {self.plan.plan_name}"
