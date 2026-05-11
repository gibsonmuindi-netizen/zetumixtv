from django.db import models


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
