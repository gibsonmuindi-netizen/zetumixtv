from django.db import models
from users.models import CustomUser
from videos.models import Video


class WatchHistory(models.Model):
    """Track user's viewing history"""
    
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='watch_history'
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='watched_by'
    )
    
    # Viewing info
    watched_at = models.DateTimeField(auto_now=True)
    minutes_watched = models.IntegerField(
        default=0,
        help_text='Number of minutes watched'
    )
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-watched_at']
        unique_together = ('user', 'video')
        verbose_name_plural = 'Watch Histories'
    
    def __str__(self):
        return f"{self.user.email} watched {self.video.title}"
