from django.contrib import admin
from .models import WatchHistory


@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'watched_at', 'minutes_watched', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('user__email', 'video__title')
    raw_id_fields = ('user', 'video')
