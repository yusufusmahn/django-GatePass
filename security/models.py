from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from account.models import UserAccount

# Create your models here.


class SecurityGuard(UserAccount):
    is_security = models.BooleanField(default=False)

