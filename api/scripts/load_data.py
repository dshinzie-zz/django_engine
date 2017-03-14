import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_engine.settings")
import django
django.setup()

import csv
from datetime import datetime

from ..models import Merchant

def load_merchants():
    path = './api/data/merchants.csv'
    with open(path, 'rb') as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)
        for row in reader:
            created = Merchant.objects.get_or_create(
                name=row[1],
                created_date=datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S %Z'),
                published_date=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S %Z')
                )

def load_all():
    load_merchants();

load_all()
