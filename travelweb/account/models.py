from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class AccountInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    groups = models.CharField(Group, max_length=20)

    def __str__(self):
        return self.username
