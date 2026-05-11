from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import WatchHistory
from .serializers import WatchHistorySerializer


class WatchHistoryListCreateView(generics.ListCreateAPIView):
    serializer_class = WatchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user).order_by('-watched_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WatchHistoryDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = WatchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user)
