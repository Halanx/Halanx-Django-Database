# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0004_cartitem_cartphoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='Cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Carts.Cart'),
        ),
    ]
