from .models import Merchant, Item
from rest_framework import viewsets, generics
from rest_framework.response import Response
from api.serializers import MerchantSerializer, ItemSerializer

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MerchantItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        merchant_id = self.kwargs['merchant_id']
        queryset = Merchant.objects.get(id=merchant_id).item_set.all()
        return queryset

class ItemMerchantViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        merchant = Item.objects.get(id=item_id).merchant
        queryset = Merchant.objects.filter(id=merchant.id)
        return queryset
