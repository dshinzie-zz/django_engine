# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170313_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit_price',
            field=models.BigIntegerField(null=True),
        ),
    ]
