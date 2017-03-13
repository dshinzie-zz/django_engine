from .models import Merchant, Item
from rest_framework import serializers


class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchant
        fields = ('name',)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'unit_price')
