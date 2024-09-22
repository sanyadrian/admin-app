from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    name = models.CharField(max_length=200)


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    username = None
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
