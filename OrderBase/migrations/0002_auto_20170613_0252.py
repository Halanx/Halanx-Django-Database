# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderBase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Items',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ItemsList.ItemList'),
        ),
    ]
