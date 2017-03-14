from .models import Merchant, Item, Invoice
from rest_framework import viewsets, generics
from rest_framework.response import Response
from api.serializers import MerchantSerializer, ItemSerializer, InvoiceSerializer, InvoiceItemSerializer, TransactionSerializer

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class MerchantInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        merchant_id = self.kwargs['merchant_id']
        queryset = Merchant.objects.get(id=merchant_id).invoice_set.all()
        return queryset

class MerchantItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        merchant_id = self.kwargs['merchant_id']
        queryset = Merchant.objects.get(id=merchant_id).item_set.all()
        return queryset

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemMerchantViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        merchant = Item.objects.get(id=item_id).merchant
        queryset = Merchant.objects.filter(id=merchant.id)
        return queryset

class ItemInvoiceItemViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        queryset = Item.objects.get(id=item_id).invoiceitem_set.all()
        return queryset

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_id']
        queryset = Invoice.objects.get(id=invoice_id).transaction_set.all()
        return queryset
