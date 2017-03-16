from .models import Merchant
from .models import Item
from .models import Invoice
from .models import Customer
from .models import InvoiceItem
from .models import Transaction
from rest_framework import viewsets, generics
from rest_framework.response import Response
from api.serializers import MerchantSerializer
from api.serializers import ItemSerializer
from api.serializers import InvoiceSerializer
from api.serializers import InvoiceItemSerializer
from api.serializers import TransactionSerializer
from api.serializers import CustomerSerializer

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

class MerchantFindViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params:
            merchant_id = self.request.query_params['id']
            queryset = Merchant.objects.filter(id=merchant_id)

        if 'name' in self.request.query_params:
            merchant_name = self.request.query_params['name']
            queryset = Merchant.objects.filter(name__iexact=merchant_name)

        return queryset

class MerchantFindAllViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params:
            merchant_id = self.request.query_params['id']
            queryset = Merchant.objects.filter(id=merchant_id)

        if 'name' in self.request.query_params:
            merchant_name = self.request.query_params['name']
            queryset = Merchant.objects.filter(name__iexact=merchant_name)

        return queryset

class MerchantRandomViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        merchant = Merchant.objects.order_by('?').first()
        queryset = Merchant.objects.filter(id=merchant.id)
        return queryset

class MerchantMostRevenueViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        quantity = self.request.query_params['quantity']
        queryset = Merchant.most_revenue(quantity)
        return queryset

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemMerchantViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        item = Item.objects.get(id=item_id).item
        queryset = Merchant.objects.filter(id=item.id)
        return queryset

class ItemInvoiceItemViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        queryset = Item.objects.get(id=item_id).invoiceitem_set.all()
        return queryset

class ItemFindViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params:
            item_id = self.request.query_params['id']
            queryset = Item.objects.filter(id=item_id)

        if 'name' in self.request.query_params:
            item_name = self.request.query_params['name']
            queryset = Item.objects.filter(name__iexact=item_name)

        return queryset

class ItemFindAllViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params:
            merchant_id = self.request.query_params['id']
            queryset = Item.objects.filter(id=merchant_id)

        if 'name' in self.request.query_params:
            merchant_name = self.request.query_params['name']
            queryset = Item.objects.filter(name__iexact=merchant_name)

        return queryset

class ItemRandomViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        item = Item.objects.order_by('?').first()
        queryset = Item.objects.filter(id=item.id)
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

class InvoiceInvoiceItemViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_id']
        queryset = Invoice.objects.get(id=invoice_id).invoiceitem_set.all()
        return queryset

class InvoiceItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_id']
        queryset = Invoice.objects.get(id=invoice_id).item_set.all()
        return queryset

class InvoiceCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_id']
        customer = Invoice.objects.get(id=invoice_id).customer
        queryset = Customer.objects.filter(id=customer.id)
        return queryset

class InvoiceMerchantItemViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_id']
        merchant = Invoice.objects.get(id=invoice_id).merchant
        queryset = Merchant.objects.filter(id=merchant.id)
        return queryset

class InvoiceFindViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params:
            invoice_id = self.request.query_params['id']
            queryset = Invoice.objects.filter(id=invoice_id)

        if 'name' in self.request.query_params:
            invoice_name = self.request.query_params['name']
            queryset = Invoice.objects.filter(name__iexact=invoice_name)

        return queryset

class InvoiceFindAllViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params:
            merchant_id = self.request.query_params['id']
            queryset = Invoice.objects.filter(id=merchant_id)

        if 'name' in self.request.query_params:
            invoice_name = self.request.query_params['name']
            queryset = Invoice.objects.filter(name__iexact=invoice_name)

        return queryset

class InvoiceRandomViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        invoice = Invoice.objects.order_by('?').first()
        queryset = Invoice.objects.filter(id=invoice.id)
        return queryset

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

class InvoiceItemInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        invoice_item_id = self.kwargs['invoice_item_id']
        invoice = InvoiceItem.objects.get(id=invoice_item_id).invoice
        queryset = Invoice.objects.filter(id=invoice.id)
        return queryset

class InvoiceItemItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        invoice_item_id = self.kwargs['invoice_item_id']
        item = InvoiceItem.objects.get(id=invoice_item_id).item
        queryset = Item.objects.filter(id=item.id)
        return queryset

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        transaction_id = self.kwargs['transaction_id']
        invoice = Transaction.objects.get(id=transaction_id).invoice
        queryset = Invoice.objects.filter(id=invoice.id)
        return queryset

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerInvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        queryset = Customer.objects.get(id=customer_id).invoice_set.all()
        return queryset

class CustomerTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        invoice_ids = Invoice.objects.filter(customer_id=customer_id).values_list('id', flat=True)
        queryset = Transaction.objects.filter(invoice_id__in=invoice_ids)
        return queryset
