from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

# Create your models here.

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class MyAccountManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None):
        if not username:
            raise ValueError(('The username must be set'))
        if not phone_number:
            raise ValueError(('The phone number must be set'))
        
        user = self.model(
            username= username,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, password):
        user = self.create_user(
            password=password,
            username=username,
            phone_number=phone_number,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
    
class PersonalData(AbstractUser):
    username= models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    country_code = models.CharField(max_length=255)
    phone_number = models.IntegerField(unique=True)
    gender = models.CharField(max_length=150, choices=GENDER,null=True, blank=True)
    birthdate = models.DateField(auto_now=False,null=True, blank=True)
    avatar = models.ImageField(upload_to='images',null=True, blank=True)
 

    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS= ['username']
    
    objects = MyAccountManager()
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)