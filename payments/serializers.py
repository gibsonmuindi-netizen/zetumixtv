from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id', 'user', 'user_email', 'amount', 'phone_number',
            'mpesa_receipt', 'mpesa_transaction_id', 'status',
            'created_at', 'updated_at',
        ]
        read_only_fields = [
            'id', 'user', 'user_email', 'mpesa_receipt',
            'mpesa_transaction_id', 'status', 'created_at', 'updated_at',
        ]
