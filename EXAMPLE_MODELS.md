"""
EXAMPLE: User Model Implementation
Follow this pattern for other models in your apps

Copy this code to: users/models.py
"""

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


# ============================================
# EXAMPLE: Video Models
# Copy this pattern to: videos/models.py
# ============================================

class Category(models.Model):
    """Video categories"""
    
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Video(models.Model):
    """Video model for streaming platform"""
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # File storage
    video_file = models.FileField(
        upload_to='videos/%Y/%m/',
        help_text='Upload video file (MP4 recommended)'
    )
    thumbnail = models.ImageField(
        upload_to='thumbnails/%Y/%m/',
        null=True,
        blank=True
    )
    
    # Video metadata
    duration = models.IntegerField(
        help_text='Duration in seconds'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='videos'
    )
    
    # Content type
    is_premium = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    # Engagement
    views = models.IntegerField(default=0)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category', '-created_at']),
            models.Index(fields=['is_premium', '-views']),
        ]
    
    def __str__(self):
        return self.title


# ============================================
# EXAMPLE: Subscription Models
# Copy this pattern to: subscriptions/models.py
# ============================================

class SubscriptionPlan(models.Model):
    """Subscription plan definitions"""
    
    PLAN_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('premium', 'Premium'),
    ]
    
    name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # In KES
    duration_days = models.IntegerField()  # How many days the subscription lasts
    features = models.TextField()  # Description of features
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return f"{self.name} - KES {self.price}"


class UserSubscription(models.Model):
    """Track user subscriptions"""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='subscription'
    )
    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )
    
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.user.email} - {self.plan.name}"


# ============================================
# EXAMPLE: Payment Models
# Copy this pattern to: payments/models.py
# ============================================

class Payment(models.Model):
    """M-Pesa payment tracking"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    subscription_plan = models.ForeignKey(
        'subscriptions.SubscriptionPlan',
        on_delete=models.SET_NULL,
        null=True
    )
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # In KES
    phone_number = models.CharField(max_length=15)
    
    # M-Pesa details
    mpesa_receipt = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount} KES"


# ============================================
# EXAMPLE: Watch History Model
# Copy this pattern to: watchhistory/models.py
# ============================================

class WatchHistory(models.Model):
    """Track what users have watched"""
    
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='watch_history'
    )
    video = models.ForeignKey(
        'videos.Video',
        on_delete=models.CASCADE,
        related_name='watched_by'
    )
    
    # Track viewing progress
    watched_duration = models.IntegerField(default=0)  # In seconds
    last_position = models.IntegerField(default=0)    # Where they stopped
    
    # Is it fully watched?
    is_completed = models.BooleanField(default=False)
    
    watched_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
        unique_together = ['user', 'video']  # One record per user per video
    
    def __str__(self):
        return f"{self.user.email} watched {self.video.title}"
