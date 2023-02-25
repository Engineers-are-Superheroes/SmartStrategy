from django.db import models

# Create your models here.

class Volunteer(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'


class Organisation_User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'username'