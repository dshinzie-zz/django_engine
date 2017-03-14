from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Merchant(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    unit_price = models.BigIntegerField(null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s %s' % (self.name, self.description, self.unit_price, self.merchant)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    merchants = models.ManyToManyField(Merchant, through='Invoice')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Invoice(models.Model):
    status = models.CharField(max_length=200)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Item, through='InvoiceItem')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.status, self.merchant, self.customer, self.merchant, self.items)

class Transaction(models.Model):
    credit_card_number = models.CharField(max_length=200)
    credit_card_expiration_date = models.DateTimeField(default=None, null=True)
    result = models.CharField(max_length=200)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s %s' % (self.credit_card_number, self.credit_card_expiration_date, self.result, self.invoice)

class InvoiceItem(models.Model):
    quantity = models.IntegerField(null=True)
    unit_price = models.BigIntegerField(null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s %s' % (self.quantity, self.unit_price, self.invoice, self.item)
