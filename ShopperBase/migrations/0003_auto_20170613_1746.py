# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopperBase', '0002_auto_20170607_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopper',
            name='PhoneNo',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='password',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
