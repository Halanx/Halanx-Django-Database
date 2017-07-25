from django.db import models


class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # UserName = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    PhoneNo = models.BigIntegerField(unique=True, null=True)

    GcmId = models.CharField(max_length=500, blank=True, null=True)

    AccessToken = models.CharField(max_length=300, blank=True, null=True)
    EmailId = models.EmailField(blank=True)
    FirstName = models.CharField(max_length=200, blank=True)
    LastName = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=1000, blank=True, null=True)
    Address = models.CharField(blank=True, null=True, max_length=300)
    logged_in = models.BooleanField(blank=True, default=True)

    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)

    AvgRating = models.FloatField(default=3.0, blank=True)
    n = models.IntegerField(default=0, blank=True)     # denotes number of times user has been rated

    def __str__(self):

        return str(self.PhoneNo)








