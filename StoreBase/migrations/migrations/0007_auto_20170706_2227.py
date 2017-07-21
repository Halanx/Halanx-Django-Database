# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopperBase', '0006_shopper_isonline'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='BankAccountNumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='BankAccountType',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='BankBranch',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='BankBranchAddress',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='BankName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='IFSCCode',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='Latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='Longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopper',
            name='VehicleSpaceAvailable',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='AvailableDate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='IsOnline',
            field=models.BooleanField(default=False),
        ),
    ]
