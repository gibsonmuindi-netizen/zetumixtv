from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from .serializers import PaymentSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all().order_by('-created_at')
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Payment.objects.all().order_by('-created_at')
        return Payment.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='pending')


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Payment.objects.all()
        return Payment.objects.filter(user=self.request.user)


class PaymentCallbackView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        mpesa_receipt = request.data.get('mpesa_receipt')
        status_value = request.data.get('status')
        mpesa_transaction_id = request.data.get('mpesa_transaction_id')

        if not mpesa_receipt or not status_value:
            return Response({'detail': 'mpesa_receipt and status are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.objects.get(mpesa_receipt=mpesa_receipt)
        except Payment.DoesNotExist:
            return Response({'detail': 'Payment not found.'}, status=status.HTTP_404_NOT_FOUND)

        payment.status = status_value
        payment.mpesa_transaction_id = mpesa_transaction_id or payment.mpesa_transaction_id
        payment.save()

        return Response({'detail': 'Payment record updated successfully.'})
