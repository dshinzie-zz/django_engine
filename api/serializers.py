from .models import Merchant, Item, Invoice, InvoiceItem, Transaction
from rest_framework import serializers

class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchant
        fields = ('id', 'name')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'unit_price')

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'status', 'customer_id', 'merchant_id')

class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ('id', 'quantity', 'unit_price', 'item_id', 'invoice_id')

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'credit_card_number', 'invoice_id', 'result')
