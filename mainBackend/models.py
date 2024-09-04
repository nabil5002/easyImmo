from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from multiupload.fields import MultiImageField,MultiFileField
from django.core.validators import FileExtensionValidator
from django.contrib.auth.hashers import check_password


# Create your models here.

class Operation(models.Model): 
    PropertyId = models.ForeignKey("Property",on_delete=models.DO_NOTHING)


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
    statusChoicesVar = [(True,'verified'),
                        (False,'unverified')]

    OwnerId = models.ForeignKey("User",on_delete=models.CASCADE, null=True, blank=True, default=None,)
    PropertyType = models.CharField(max_length=30)
    PropertyImages = models.FileField(upload_to='property_files/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png','jpeg'])], blank=True, null=True)
    PropertyOwningFiles = models.FileField(upload_to='propertyOwning_files/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png','pdf','jpeg'])], blank=True, null=True,)
    PropertyPrice = models.IntegerField();
    PropertyName = models.CharField(max_length=50)
    PropertyLocation = models.CharField(max_length=50)
    verificationStatus = models.BooleanField(choices=statusChoicesVar ,default=False)

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
    ContractType = models.CharField(max_length=100)
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



class Poster(models.Model):
    PosterPicture = models.FileField()
    PosterHeader = models.CharField(max_length=50)
    PosterText = models.TextField()

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Poster'
        verbose_name_plural = 'Posters'
        
class PropertyNotification(models.Model):
    PropertyId = models.ForeignKey("Property",on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        pass

class UserNotification(models.Model):
    UserId = models.ForeignKey("User",on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        pass
# authentification models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    def get_user_by_email(self, email):
        try:
            return self.get(email=email)
        except self.model.DoesNotExist:
            return None

class User(AbstractBaseUser, PermissionsMixin):
    UserId = models.AutoField(primary_key=True)
    UserStatus = models.CharField(max_length=10, choices=[('Owner', 'Owner'), ('Buyer', 'Buyer'),('Admin','Admin')])
    SureName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    UserProfilePhoto = models.FileField(upload_to='property_files/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])], blank=True, null=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    UserNumber = models.IntegerField( null=True, blank=True)
    UserRequiresUplaod = models.FileField(upload_to='property_files/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'pdf', 'doc'])], blank=True, null=True)

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


