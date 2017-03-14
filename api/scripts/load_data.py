import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_engine.settings")
import django
django.setup()

import csv
from datetime import datetime

from ..models import Merchant, Item

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

def load_all():
    load_merchants();
    load_items();

load_all()
