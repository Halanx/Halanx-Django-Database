from __future__ import unicode_literals

from django.db import models
from ShopperBase.models import Shopper
from OrderBase.models import Order


class Batch(models.Model):

    ShopperId = models.ForeignKey(Shopper, blank=True, null=True)
    Earnings = models.FloatField(blank=True, default=0.0)

    PermanentShopper = models.BigIntegerField(blank=True, null=True)
    PermanentAvailable = models.BooleanField(blank=True, default=False)

    TemporaryShopper = models.BigIntegerField(blank=True, null=True)
    TemporaryAvailable = models.BooleanField(blank=True, default=False)

    CentroidLatitude = models.FloatField(blank=True, null=True)
    CentroidLongitude = models.FloatField(blank=True, null=True)

    IsDelivered = models.BooleanField(blank=True, default=False)
    Size = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.ShopperId)

    def save(self, *args, **kwargs):

        super(Batch, self).save(*args, **kwargs)