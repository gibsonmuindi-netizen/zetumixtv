from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('', views.VideoListView.as_view(), name='video-list'),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
]