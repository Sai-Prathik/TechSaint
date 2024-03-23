from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=500,blank=True)
    phone = models.CharField(blank=True) 
    username = models.CharField(max_length=20,unique=False,blank=True)
    email = models.EmailField ( unique=True, max_length=254, verbose_name='email address')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []