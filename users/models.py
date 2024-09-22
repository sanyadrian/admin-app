from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []