from .models import Merchant, Item, Invoice
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
