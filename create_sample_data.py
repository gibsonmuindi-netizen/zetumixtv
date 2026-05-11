import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'streaming_platform.settings')
django.setup()

from videos.models import Category, Video

# Create sample categories
categories_data = [
    {'name': 'Education', 'slug': 'education', 'description': 'Educational content for learning'},
    {'name': 'Entertainment', 'slug': 'entertainment', 'description': 'Fun and entertainment videos'},
    {'name': 'Music', 'slug': 'music', 'description': 'Kenyan music and performances'},
    {'name': 'Culture', 'slug': 'culture', 'description': 'Cultural content and traditions'},
]

for cat_data in categories_data:
    Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults=cat_data
    )

# Create sample videos
videos_data = [
    {
        'title': 'Introduction to Kenyan History',
        'description': 'Learn about the rich history of Kenya from ancient times to modern day.',
        'duration': 1800,  # 30 minutes
        'category_slug': 'education',
        'is_premium': False,
    },
    {
        'title': 'Traditional Kenyan Music Performance',
        'description': 'Watch an amazing performance of traditional Kenyan music and dance.',
        'duration': 2400,  # 40 minutes
        'category_slug': 'music',
        'is_premium': False,
    },
    {
        'title': 'Kenyan Wildlife Documentary',
        'description': 'Explore the amazing wildlife in Kenya\'s national parks.',
        'duration': 3600,  # 1 hour
        'category_slug': 'entertainment',
        'is_premium': True,
    },
    {
        'title': 'Swahili Language Lesson',
        'description': 'Learn basic Swahili phrases for everyday conversation.',
        'duration': 1200,  # 20 minutes
        'category_slug': 'education',
        'is_premium': False,
    },
]

for video_data in videos_data:
    category = Category.objects.get(slug=video_data.pop('category_slug'))
    Video.objects.get_or_create(
        title=video_data['title'],
        defaults={
            **video_data,
            'category': category,
        }
    )

print("Sample data created successfully!")