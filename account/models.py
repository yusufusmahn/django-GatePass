from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserAccount(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)