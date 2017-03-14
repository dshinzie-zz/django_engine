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


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
