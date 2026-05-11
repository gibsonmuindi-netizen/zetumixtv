from django.urls import path
from . import views

urlpatterns = [
    path('', views.WatchHistoryListCreateView.as_view(), name='watchhistory-list'),
    path('<int:pk>/', views.WatchHistoryDetailView.as_view(), name='watchhistory-detail'),
]
