# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserBase', '0009_user_logged_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
