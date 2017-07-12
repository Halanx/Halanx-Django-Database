from django.db import models
from ShopperBase.models import Shopper
# from BatchBase.models import Batch
from Halanx import settings
from UserBase.models import User


RatingChoice = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

# Problem : How to update shopper and user ratings after order is delivered ?   Done


class Order (models.Model):

    # ListId = models.OneToOneField(OrderList, unique=True, blank=True)
    #  maybe not needed cos pk of class would have the same function

    # Items = models.OneToOneField(ItemList, blank=True, null=True)                # check

    # Items = models.OneToOneField(ItemList, blank=True)                # check

    # Customer = models.ForeignKey(User, null=True, blank=True)
    # BatchId = models.ForeignKey(Batches, null=True,  blank=True)
    # ShopperId = models.ForeignKey(Shopper, null=True, blank=True)

    # these three fields are giving error 'long' object has no field 'customer'

    # SPECIFICS
    CustomerPhoneNo = models.BigIntegerField(null=True)
    PlacingTime = models.DateTimeField(auto_now_add=True)

    # MONEY INVOLVED
    Total = models.FloatField(blank=True, null=True)
    DeliveryCharges = models.FloatField(null=True, blank=True, default=0.0)
    Earnings = models.FloatField(null=True, blank=True, default=0.0)

    # WHERE TO DELIVER
    DeliveryAddress = models.CharField(max_length=300, null=True, blank=True)
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)

    # RATINGS EARNED
    UserRating = models.FloatField(choices=RatingChoice, default=3.0)
    ShopperRating = models.FloatField(choices=RatingChoice, default=3.0)

    # DELIVERY STATUS
    IsDelivered = models.BooleanField(default=False, blank=True)

    # DELIVERY TIME
    DeliveryDate = models.CharField(max_length=20, null=True, blank=True)
    StartTime = models.TimeField(null=True, blank=True)
    EndTime = models.TimeField(null=True, blank=True)

    # EXTRAS
    Notes = models.TextField(null=True, blank=True)
    PriorityScore = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return str(self.id)


    """
    def save(self, *args, **kwargs):  # override save function of model class
        # self.Total = self.Items.Total
        # attach code for earnings of shopper in this order

        if self.IsDelivered:
            temp = self.ShopperId.AvgRating*self.ShopperId.n
            # temp1 = self.Items.Customer.AvgRating*self.Items.Customer.n
            self.ShopperId.n +=1
            # self.Items.Customer.n +=1
            temp += self.ShopperRating
            temp1 += self.UserRating
            self.ShopperId.AvgRating /= self.ShopperId.n
            self.Items.Customer.AvgRating /=self.Items.Customer.n

        self.BatchId.Earning += self.Earnings
        super(Order, self).save(*args, **kwargs)

    """
















