from django.db import models


# Create your models here.
class Ledgers(models.Model):
    date = models.DateField()
    debit = models.IntegerField()
    credit = models.IntegerField()
    balance = models.IntegerField()
    description = models.CharField(max_length=150)
