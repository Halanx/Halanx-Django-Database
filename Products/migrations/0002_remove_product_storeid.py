# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='StoreId',
        ),
    ]
