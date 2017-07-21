# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopperBase', '0004_documents_squashed_0005_auto_20170615_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='AccessToken',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='A',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='B',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='C',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='D',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='E',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='IdType',
            field=models.CharField(blank=True, choices=[(b'Aadhar Card', b'Aadhar Card'), (b'Voter Id Card', b'Voter Id Card')], default=b'Aadhar Card', max_length=100),
        ),
    ]
