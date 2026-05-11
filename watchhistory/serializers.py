from rest_framework import serializers
from .models import WatchHistory


class WatchHistorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = WatchHistory
        fields = [
            'id', 'user', 'user_email', 'video',
            'watched_at', 'minutes_watched', 'is_completed',
        ]
        read_only_fields = ['id', 'user', 'user_email', 'watched_at']
