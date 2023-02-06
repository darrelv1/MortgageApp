from xml.dom import ValidationErr
from django.db import models
from django.core.exceptions import ValidationError
from .BaseApp.Profiles import UserInvestor


# Create your models here.
class Ledger(models.Model):
    date = models.DateField(null=True)
    debit = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    description = models.CharField(null=True, max_length=150)
    

    def __str__(self):
        return f"{self.description}"

    def set_balance(self):
        prevBalance = Ledger.objects.order_by('id').last().balance
        if self.debit == None:
            self.debit = 0
        elif self.credit == None:
            self.credit = 0
        netAmount = self.debit - self.credit
        self.balance = prevBalance + netAmount

    def save(self, *args, **kwargs):
        if Ledger.objects.all().exists():
            self.set_balance()
        else: 
            self.balance = self.debit - self.credit
        super().save(*args, **kwargs)


def getLastItem():
    lastitem = Ledger.objects.order_by('id').last()
    return lastitem.balance




class UserProfile(models.Model):
    name = models.CharField(max_length=150)
    rate = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.name}"
    
    #no more than 3 users
    def save(self, *args, **kwargs):
        count = UserProfile.objects.all().count()
        max_objects = 3
        if count == max_objects: 
            raise  ValidationError("You have reached the maximum number of users")
        super().save(*args, **kwargs)


class AppLedger(models.Model):
    date = models.DateField(null=True)
    debit = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)
    balance = models.IntegerField(default=False, null=True)
    description = models.CharField(null=True, max_length=150)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE,null=True, blank=True, related_name='%(class)s')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)


    class Meta: 
        abstract = True
        ordering = ['date']

    def __str__(self):
        return f"Description: {self.description}, Current Balance: {self.balance} and the Date of this transaction was {self.date}"

    def set_balance(self):
        prevBalance = self.__class__.objects.order_by('id').last().balance
        if self.debit == None:
            self.debit = 0
        elif self.credit == None:
            self.credit = 0
        netAmount = self.debit - self.credit
        self.balance = prevBalance + netAmount

    def save(self, *args, **kwargs):
        if self.__class__.objects.all().exists():
            self.set_balance()
        else: 
            self.balance = self.debit - self.credit

        count = self.__class__.objects.all().count()
        if count >= 1: 
            prevUser = self.__class__.objects.order_by('id').first().user
            self.user = prevUser
        super().save(*args, **kwargs)



class userLedger1(AppLedger):
    pass
   
class userLedger2(AppLedger):
    pass
  
class userLedger3(AppLedger):
     pass
   


    




  
        

        



