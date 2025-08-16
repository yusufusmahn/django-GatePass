from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from account.models import UserAccount

# Create your models here.



class Resident(UserAccount):
    is_resident = models.BooleanField(default=False)


class House(models.Model):
    house_number = models.PositiveIntegerField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    resident = models.ForeignKey(Resident, on_delete=models.PROTECT)


class Invite(models.Model):
    code = models.CharField(max_length=10, unique=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=False, blank=False)
    status = models.BooleanField(default=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT)


class Visitor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=True, null=True)
    invite = models.ForeignKey(Invite, on_delete=models.PROTECT)


