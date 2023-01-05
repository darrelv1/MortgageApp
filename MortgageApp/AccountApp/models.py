from django.db import models


# Create your models here.
class Ledgers(models.Model):
    date = models.DateField()
    debit = models.IntegerField()
    credit = models.IntegerField()
    balance = models.IntegerField(default=False)
    description = models.CharField(null=True, max_length=150)

    def __str__(self):
        return f"{self.description}"