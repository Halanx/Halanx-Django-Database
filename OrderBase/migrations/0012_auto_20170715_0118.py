# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-14 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderBase', '0011_auto_20170713_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='DeliveryDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
