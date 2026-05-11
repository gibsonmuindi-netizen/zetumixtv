from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'phone_number', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__email', 'mpesa_receipt', 'mpesa_transaction_id', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
