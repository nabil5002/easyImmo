from django.db import models

# Create your models here.

class Operation(models.Model):
    PropertyId = models.AutoField(primary_key=True)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'

class Sell(Operation):
    SellPrice = models.IntegerField()
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sell'
        verbose_name_plural = 'Sells'

class Rental(Operation):
    RentPrice = models.IntegerField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Rental'
        verbose_name_plural = 'Rentals'

class Property(models.Model):
    Propertype = models.CharField(max_length=30)
    PropertyName = models.CharField(max_length=50)
    PropertyLocation = models.CharField(max_length=50)

    def __str__(self):
        pass

    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'Property'
    #     verbose_name_plural = 'Propertys'

class EstateOfficer(models.Model):
    OfficerName = models.CharField(max_length=50)
    OfficerNumber = models.CharField(max_length=50)
    OfficerMail = models.EmailField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'AgentImma'
        verbose_name_plural = 'AgentImmas'

class Transaction(models.Model):
    propertytId = models.ForeignKey("Operation", on_delete=models.DO_NOTHING)
    Amount = models.PositiveBigIntegerField()
    Status = models.BooleanField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

class Contract(models.Model):
    ContractType = models.CharField()
    SignatureDate = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

class Visit(models.Model):
    PropertyId = models.ForeignKey("Operation",on_delete=models.DO_NOTHING)
    Costs = models.IntegerField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'

class EvaluateProperty(models.Model):
    Description = models.TextField(max_length=200)
    status = models.BooleanField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'EvaluateProperty'
        verbose_name_plural = 'EvaluatePropertys'

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=50)
    UserProfilePhoto = models.FileField(upload_to="")
    UserPwd = models.CharField(max_length=50)
    UserMail  = models.EmailField()
    UserNumber = models.IntegerField()
    # UserUplaod = models.Multiple
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Owner(User):
    statusChoicesVar = [(True,'Owner'),
                        (False,'buyer')]
    UserStatus = models.BooleanField(choices=statusChoicesVar)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

class buyer(User):
    statusChoicesVar = [(True,'Owner'),
                        (False,'buyer')]
    UserStatus = models.BooleanField(choices=statusChoicesVar)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'buyer'
        verbose_name_plural = 'buyers'

class Poster(models.Model):
    PosterPicture = models.FileField()
    PosterHeader = models.CharField()
    PosterText = models.TextField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Poster'
        verbose_name_plural = 'Posters'