from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'merchants', views.MerchantViewSet)
router.register(r'merchants/(?P<merchant_id>\d+)/items', views.MerchantItemViewSet, 'Merchant')
router.register(r'merchants/(?P<merchant_id>\d+)/invoices', views.MerchantInvoiceViewSet, 'Merchant')

router.register(r'items', views.ItemViewSet)
router.register(r'items/(?P<item_id>\d+)/merchant', views.ItemMerchantViewSet, 'Item')
router.register(r'items/(?P<item_id>\d+)/invoice_items', views.ItemInvoiceItemViewSet, 'Item')

router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoices/(?P<invoice_id>\d+)/transactions', views.InvoiceTransactionViewSet, 'Invoice')
router.register(r'invoices/(?P<invoice_id>\d+)/invoice_items', views.InvoiceInvoiceItemViewSet, 'Invoice')
router.register(r'invoices/(?P<invoice_id>\d+)/items', views.InvoiceItemViewSet, 'Invoice')
router.register(r'invoices/(?P<invoice_id>\d+)/customer', views.InvoiceCustomerViewSet, 'Invoice')
router.register(r'invoices/(?P<invoice_id>\d+)/merchant', views.InvoiceMerchantItemViewSet, 'Invoice')

router.register(r'invoice_items', views.InvoiceItemViewSet)
router.register(r'invoice_items/(?P<invoice_item_id>\d+)/invoice', views.InvoiceItemInvoiceViewSet, 'InvoiceItem')
router.register(r'invoice_items/(?P<invoice_item_id>\d+)/item', views.InvoiceItemItemViewSet, 'InvoiceItem')

router.register(r'transactions', views.TransactionViewSet)
router.register(r'transactions/(?P<transaction_id>\d+)/invoice', views.TransactionInvoiceViewSet, 'Transaction')

router.register(r'customers', views.CustomerViewSet)
router.register(r'customers/(?P<customer_id>\d+)/invoices', views.CustomerInvoiceViewSet, 'Customer')
router.register(r'customers/(?P<customer_id>\d+)/transactions', views.CustomerTransactionViewSet, 'Customer')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
