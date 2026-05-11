from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.SubscriptionPlanListView.as_view(), name='subscription-plan-list'),
    path('current/', views.UserSubscriptionDetailView.as_view(), name='user-subscription-detail'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
]
