from django.db import models
from ..ProfileApp.models import Users


# Create your models here.
class Ledgers(models.Model):
    date = models.DateField()
    debit = models.IntegerField()
    credit = models.IntegerField()
    balance = models.IntegerField(default=False)
    description = models.CharField(null=True, max_length=150)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"