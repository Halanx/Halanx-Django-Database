from __future__ import unicode_literals

from django.db import models
from ShopperBase.models import Shopper
from OrderBase.models import Order


class Batch(models.Model):

    ShopperId = models.ForeignKey(Shopper, blank=True)
    Earnings = models.FloatField(blank=True, default=0.0)
    OrderNo = models.ForeignKey(Order, null=True, blank=True)

    PermanentShopper = models.BigIntegerField(blank=True, null=True)
    PermanentAvailable = models.BigIntegerField(blank=True, default=False)

    TemporaryShopper = models.BigIntegerField(blank=True, null=True)
    TemporaryAvailable = models.BigIntegerField(blank=True, default=False)

    IsDelivered = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return str(self.OrderNo)

    def save(self, *args, **kwargs):

        onlineshoppers = Shopper.objects.filter(IsOnline=True, Verified=True)
        if onlineshoppers:
            self.ShopperId = onlineshoppers[0]
            print len(onlineshoppers)

        self.ShopperPhoneNo = self.ShopperId.PhoneNo
        super(Batch, self).save(*args, **kwargs)



