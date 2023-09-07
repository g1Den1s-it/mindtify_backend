from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """User model"""
    image = models.ImageField(upload_to="user/image/")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']