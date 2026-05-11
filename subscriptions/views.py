from datetime import timedelta
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SubscriptionPlan, UserSubscription
from .serializers import SubscriptionPlanSerializer, UserSubscriptionSerializer


class SubscriptionPlanListView(generics.ListAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAuthenticated]


class UserSubscriptionDetailView(generics.RetrieveAPIView):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.user_subscription


class SubscribeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        plan_id = request.data.get('plan_id')

        if not plan_id:
            return Response({'detail': 'plan_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            plan = SubscriptionPlan.objects.get(pk=plan_id)
        except SubscriptionPlan.DoesNotExist:
            return Response({'detail': 'Subscription plan not found.'}, status=status.HTTP_404_NOT_FOUND)

        end_date = timezone.now() + timedelta(days=plan.duration_days)
        subscription, _ = UserSubscription.objects.update_or_create(
            user=request.user,
            defaults={
                'plan': plan,
                'end_date': end_date,
                'is_active': True,
                'auto_renew': True,
            },
        )

        request.user.subscription_status = plan.plan_name
        request.user.subscription_end_date = end_date
        request.user.save()

        return Response(UserSubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)
