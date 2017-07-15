from django.db import models
from Halanx import settings

AAD = 'Aadhar Card'
VID = 'Voter Id Card'
IdentityProofs = (
    (AAD, 'Aadhar Card'),
    (VID, 'Voter Id Card'),
)


CAR = 'Car'
Vehicles = (
    (CAR, 'Car'),
)


class Shopper(models.Model):

    # PERSONAL DETAILS
    # add photo ?
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    PhoneNo = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=1000, blank=True, null=True)
    EmailId = models.EmailField(blank=True)
    City = models.CharField(max_length=200, null=True, blank=True, default='Delhi')
    DisplayPictureURL = models.CharField(max_length=300, blank=True, null=True)
    AccessToken = models.CharField(max_length=300, blank=True, null=True)
    GcmId = models.CharField(max_length=500, blank=True, null=True)

    # ID DETAILS
    IdNumber = models.CharField(max_length=50, blank=True)                             # number of id
    IdType = models.CharField(max_length=100, blank=True, default='Aadhar Card')

    # VEHICLE DETAILS
    Vehicle = models.CharField(max_length=50, blank=True, default='Car')
    VehicleSpaceAvailable = models.IntegerField(default=3, blank=True, null=True)

    # AVAILABILITY DETAILS
    AvailableDate = models.DateField(max_length=20, blank=True, null=True)
    AvailableFrom = models.TimeField(blank=True, null=True)
    AvailableTo = models.TimeField(blank=True, null=True)
    IsOnline = models.BooleanField(blank=True, default=False)
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)

    # BANK DETAILS
    BankAccountNumber = models.CharField(max_length=50, blank=True, null=True)
    BankAccountType = models.CharField(max_length=10, blank=True, null=True)
    BankName = models.CharField(max_length=200, blank=True, null=True)
    BankBranch = models.CharField(max_length=300, blank=True, null=True)
    BankBranchAddress = models.CharField(max_length=300, blank=True, null=True)
    IFSCCode = models.CharField(max_length=25, blank=True, null=True)

    # RATINGS DETAILS
    AvgRating = models.FloatField(default=3.0, blank=True, null=True)
    n = models.IntegerField(default=0, blank=True)
    A = models.FloatField(blank=True, default=0)
    B = models.FloatField(blank=True, default=0)
    C = models.FloatField(blank=True, default=0)
    D = models.FloatField(blank=True, default=0)
    E = models.FloatField(blank=True, default=0)

    Verified = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return str(self.PhoneNo)


class Documents(models.Model):

    ShopperPhoneNo = models.BigIntegerField(unique=True)

    AadharImage = models.TextField(blank=True, null=True)
    LicenseImage = models.TextField(blank=True, null=True)
    VehicleRCImage = models.TextField(blank=True, null=True)

    AadharURL = models.CharField(max_length=500, blank=True, null=True)
    LicenseURL = models.CharField(max_length=500, blank=True, null=True)
    VehicleRCURL = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.ShopperPhoneNo)


class ShopperImage(models.Model):

    ShopperPhoneNo = models.BigIntegerField(unique=True)

    DisplayPicture = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.ShopperPhoneNo)



















