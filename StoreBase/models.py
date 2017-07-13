from django.db import models


class Store(models.Model):

    # NAME, ADDRESS OF STORE
    StoreName = models.CharField(blank=True, null=True, max_length=200)
    StoreAddress = models.CharField(max_length=300, null=True, blank=True)
    StoreLogo = models.CharField(max_length=300, null=True, blank=True)

    # DEALER DETAILS
    Dealer_FirstName = models.CharField(max_length=200, null=True, blank=True)
    Dealer_LastName = models.CharField(max_length=200, null=True, blank=True)
    Dealer_ContactNo = models.BigIntegerField(null=True, blank=True)
    Dealer_EmailId = models.EmailField(blank=True, null=True)
    Dealer_password = models.CharField(max_length=1000, blank=True, null=True)
    Dealer_Designation = models.CharField(max_length=100, blank=True, null=True)

    # LOCATION DETAILS
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)

    # BUSINESS DETAILS
    CompanyLegalName = models.CharField(max_length=300, blank=True, null=True)
    PANNumber = models.CharField(max_length=50, blank=True, null=True)

    # BANK ACCOUNTS DETAILS
    BankAccountNumber = models.CharField(max_length=50, blank=True, null=True)
    BankAccountType = models.CharField(max_length=10, blank=True, null=True)
    BankName = models.CharField(max_length=200, blank=True, null=True)
    BankBranch = models.CharField(max_length=300, blank=True, null=True)
    BankBranchAddress = models.CharField(max_length=300, blank=True, null=True)
    IFSCCode = models.CharField(max_length=25, blank=True, null=True)

    # STORE OPENING TIMINGS
    MondayOpeningTime = models.TimeField(blank=True, null=True)
    TuesdayOpeningTime = models.TimeField(blank=True, null=True)
    WednesdayOpeningTime = models.TimeField(blank=True, null=True)
    ThursdayOpeningTime = models.TimeField(blank=True, null=True)
    FridayOpeningTime = models.TimeField(blank=True, null=True)
    SaturdayOpeningTime = models.TimeField(blank=True, null=True)
    SundayOpeningTime = models.TimeField(blank=True, null=True)

    # STORE CLOSING TIMINGS
    MondayClosingTime = models.TimeField(blank=True, null=True)
    TuesdayClosingTime = models.TimeField(blank=True, null=True)
    WednesdayClosingTime = models.TimeField(blank=True, null=True)
    ThursdayClosingTime = models.TimeField(blank=True, null=True)
    FridayClosingTime = models.TimeField(blank=True, null=True)
    SaturdayClosingTime = models.TimeField(blank=True, null=True)
    SundayClosingTime = models.TimeField(blank=True, null=True)

    Active = models.BooleanField(blank=True, default=True)              # don't know if this is required or not
                                                            # as if store is deleted all its products will be too

    def __str__(self):
        return self.StoreName


class Logo(models.Model):

    StoreId = models.IntegerField(unique=True, blank=True, null=True)

    StoreLogoImage = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.StoreId)




























