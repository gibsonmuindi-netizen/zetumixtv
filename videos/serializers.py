from rest_framework import serializers
from .models import Video, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']


class VideoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Video
        fields = [
            'id', 'title', 'description', 'video_file', 'thumbnail',
            'duration', 'category', 'category_name', 'is_premium',
            'is_published', 'created_at', 'views'
        ]
        read_only_fields = ['id', 'created_at', 'views']