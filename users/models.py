from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    Adds fields specific to the streaming platform
    """
    
    # Email field (required)
    email = models.EmailField(unique=True)
    
    # Phone number for M-Pesa
    phone_number = models.CharField(
        max_length=15, 
        unique=True,
        null=True,
        blank=True
    )
    
    # Subscription status
    SUBSCRIPTION_CHOICES = [
        ('free', 'Free'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('premium', 'Premium'),
    ]
    subscription_status = models.CharField(
        max_length=20,
        choices=SUBSCRIPTION_CHOICES,
        default='free'
    )
    
    # When subscription ends
    subscription_end_date = models.DateTimeField(
        null=True,
        blank=True
    )
    
    # User profile
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email
    
    def is_subscribed(self):
        """Check if user has active subscription"""
        from django.utils import timezone
        if self.subscription_status == 'free':
            return False
        if self.subscription_end_date:
            return self.subscription_end_date > timezone.now()
        return False
