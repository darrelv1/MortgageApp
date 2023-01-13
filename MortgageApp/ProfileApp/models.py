from django.db import models
from ..AccountApp.models import Ledgers

class Users (models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(0)




# Create your models here.
