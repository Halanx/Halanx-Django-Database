from django.db import models
from Products.models import Product
from UserBase.models import User
from OrderBase.models import Order


class OrderItem(models.Model):

    OList = models.ForeignKey(Order, null=True, blank=True, related_name="items")    # add on_delete cascade
    # Item = models.ForeignKey(Product, blank=True, null=True)
    Item = models.IntegerField(blank=True, null=True)
    Quantity = models.FloatField(blank=True, default=1.0)                   # may be decimal also check
    SubTotal = models.FloatField(blank=True, null=True)
    Notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.OList) + " : " + str(self.id)




"""
class OrderList(models.Model):             #object of this class shall be made as soon as the order is placed

    Total = models.FloatField(blank=True, default=0.0)
    DeliveryCharges = models.FloatField(blank=True, default=0.0)
    timestamp = models.DateTimeField(blank=True, auto_now=True)  # timestamp change as soon as cart changes

    def __str__(self):
        return str(self.pk)


    def save(self, *args, **kwargs):
        g = User.objects.get(PhoneNo=self.UserPhone)
        self.Username = g

        # attach algo for delivery charges
        super(Cart, self).save(*args, **kwargs)

"""




