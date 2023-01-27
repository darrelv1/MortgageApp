from django.db import models



# Create your models here.
class Ledger(models.Model):
    date = models.DateField(null=True)
    debit = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)
    balance = models.IntegerField(default=False)
    description = models.CharField(null=True, max_length=150)

    def __str__(self):
        return f"{self.description}"


class AppLedger(models.Model):
    date = models.DateField(null=True)
    debit = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)
    balance = models.IntegerField(default=False, null=True)
    description = models.CharField(null=True, max_length=150)

    def __str__(self):
        return f"{self.description}"


class AppProfile(models.Model):
    name = models.CharField(max_length=150)
    ledger = models.OneToOneField(
        AppLedger,
        on_delete=models.CASCADE,
        primary_key=True,

    )

    def __str__(self):
        return f"{self.name}"


class UserProfile(models.Model):
    name = models.CharField(max_length=150)
    rate = models.IntegerField(null=True)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
