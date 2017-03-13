from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Merchant(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    unit_price = models.BigIntegerField
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
