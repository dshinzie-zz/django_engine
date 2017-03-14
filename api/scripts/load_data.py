import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_engine.settings")
import django
django.setup()

import csv
from datetime import datetime

from ..models import Merchant, Item, Customer, Invoice, Transaction, InvoiceItem

def load_merchants():
    path = './api/data/merchants.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = Merchant.objects.get_or_create(
                id=row[0],
                name=row[1],
                created_date=datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_items():
    path = './api/data/items.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = Item.objects.get_or_create(
                id=row[0],
                name=row[1],
                description=row[2],
                unit_price=row[3],
                merchant_id=row[4],
                created_date=datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_customers():
    path = './api/data/customers.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = Customer.objects.get_or_create(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                created_date=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_invoices():
    path = './api/data/invoices.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = Invoice.objects.get_or_create(
                id=row[0],
                customer_id=row[1],
                merchant_id=row[2],
                status=row[3],
                created_date=datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_transactions():
    path = './api/data/transactions.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = Transaction.objects.get_or_create(
                id=row[0],
                invoice_id=row[1],
                credit_card_number=row[2],
                credit_card_expiration_date=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S %Z') if len(row[3]) > 0 else None,
                result=row[4],
                created_date=datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_invoice_items():
    path = './api/data/invoice_items.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = InvoiceItem.objects.get_or_create(
                id=row[0],
                item_id=row[1],
                invoice_id=row[2],
                quantity=(row[3]),
                unit_price=row[4],
                created_date=datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_all():
    load_merchants()
    load_items()
    load_customers()
    load_invoices()
    load_transactions()
    load_invoice_items()

load_all()
