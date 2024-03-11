from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import AccountManager


class Account(AbstractUser):
    first_name = None
    last_name = None

    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=150)

    objects = AccountManager()

    def __str__(self):
        return self.email
