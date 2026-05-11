#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'streaming_platform.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

django.setup()

from django.contrib.auth import get_user_model
from videos.models import Category, Video
from subscriptions.models import SubscriptionPlan

User = get_user_model()

# Create sample superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@streamingplatform.com',
        password='admin123',
    )
    print('✓ Admin user created')

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
print('✓ Categories created')

# Create sample subscription plans
plans_data = [
    {'plan_name': 'free', 'price': '0', 'duration_days': 30, 'description': 'Free tier'},
    {'plan_name': 'weekly', 'price': '99', 'duration_days': 7, 'description': 'Weekly subscription'},
    {'plan_name': 'monthly', 'price': '299', 'duration_days': 30, 'description': 'Monthly subscription with HD'},
    {'plan_name': 'premium', 'price': '899', 'duration_days': 30, 'description': 'Premium with offline downloads'},
]

for plan_data in plans_data:
    SubscriptionPlan.objects.get_or_create(
        plan_name=plan_data['plan_name'],
        defaults={
            'price': plan_data['price'],
            'duration_days': plan_data['duration_days'],
            'description': plan_data['description'],
            'includes_hd': plan_data['plan_name'] in ['monthly', 'premium'],
            'max_streams': 4 if plan_data['plan_name'] == 'premium' else 1,
            'includes_offline': plan_data['plan_name'] == 'premium',
        }
    )
print('✓ Subscription plans created')

print('\n✅ Database setup complete!')
print('Admin credentials: admin / admin123')
