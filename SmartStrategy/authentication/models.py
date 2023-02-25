from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    skills = models.CharField(max_length=255, default="")
    #put keywords


class Organisation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    
