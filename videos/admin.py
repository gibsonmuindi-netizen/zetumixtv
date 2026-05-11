from django.contrib import admin
from .models import Category, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_premium', 'views', 'created_at')
    list_filter = ('is_published', 'is_premium', 'category')
    search_fields = ('title', 'description')
    raw_id_fields = ('category',)
