from django.db import models
from Products.models import Product
from UserBase.models import User


class CartItem(models.Model):
    Cart = models.ForeignKey('Cart', null=True, blank=True, related_name="carts")    # add on_delete cascade
    Item = models.ForeignKey(Product)
    CartPhoneNo = models.BigIntegerField(blank=True, null=True)   # phone of User

    Quantity = models.FloatField(blank=True, default=1.0)                   # may be decimal also check
    SubTotal = models.FloatField(blank=True, null=True)
    Notes = models.TextField(null=True, blank=True)
    Active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.SubTotal = self.Item.Price * self.Quantity
        g = Cart.objects.get(UserPhone=self.CartPhoneNo)
        self.Cart = g
        self.Cart.Total = self.Cart.Total + (self.Item.Price*self.Quantity)
        self.Cart.save()
        # self.CartNo = self.Cart.pk
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Cart.UserPhone) + " : " + str(self.Item.pk)


class Cart(models.Model):             # object of this class shall be updated as soon as user changes his cart

    Username = models.OneToOneField(User, blank=True, null=True)
    Total = models.FloatField(blank=True, default=0.0)

    UserPhone = models.BigIntegerField(unique=True, null=True, blank=True)

    DeliveryCharges = models.FloatField(blank=True, default=0.0)
    timestamp = models.DateTimeField(blank=True, auto_now=True)     # timestamp change as soon as cart changes
    Active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return str(self.Username.PhoneNo)

    def save(self, *args, **kwargs):

        g = User.objects.get(PhoneNo=self.UserPhone)
        self.Username = g

        # attach algo for delivery charges
        super(Cart, self).save(*args, **kwargs)














