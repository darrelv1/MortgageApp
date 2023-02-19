from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import ManyToOneRel


from ..models import Ledger, userLedger1, userLedger2, userLedger3, AppLedger, UserProfile
#Custome Built Serializers
from ..serializers import (AccountSerializer
                        ,CreateAccountSerializer
                        ,DeleteAccountSerializer
                        ,UserLedgerSerializer
                        ,CreateUserLedgerSerializer
                        ,CreateUserLedgerSerializer2
                        ,DeleteUserLedSerializer
                        ,splitSerializer
                        )
#Django provide serializers
from django.core.serializers import serialize

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

import json



"""GENERIC HELPERS"""

#plug-in pass through mutiple params 
def call_function(func, *args,):
        return func(*args)



#mini-func get target object
def get_SpecificLedgerID_by(MDL, field, value):

    switcher = {
        "id" : MDL.objects.get(id = int(value) if type(value) == str else value) or None
    }
    product = switcher.get(field)
    return  product


   
def get_LedgerRelated(MDL):
  
    pass


#mini-func get target object
def get_SpecificLedgerID(MDL, id):
    return  MDL.objects.get(id = id)

#Get Related_Names from the Many to One
def get_relatedNames_Many2One(MDL):  
  ledger_fields = MDL._meta.get_fields()
  related_names = []

  for field in ledger_fields:
    if isinstance(field, ManyToOneRel):
        related_names.append(field.related_name)

  return related_names

#Constructing AppLedgers    
def getAppLedgers(): 
    subclasses = AppLedger.__subclasses__()
    container = [miniledger for miniledger in subclasses]
    return container 

#applying function to each subclass of AppLedger
def getAppLedgersF(func): 
    subclasses = AppLedger.__subclasses__()
    container = [func(miniledger) for miniledger in subclasses]
    return container 

#applying function to each subclass of AppLedger and the main Ledger
def getLedgersF(func): 
    subclasses = AppLedger.__subclasses__()
    allLedgers = [ ele for ele in subclasses]
    allLedgers.append(Ledger)
    container = [func(ledger) for ledger in allLedgers]
    return container 
  

#All data deleted
def genericDeleteAll(MDL):
    desc = MDL.__str__()
    MDL.objects.all().delete()
    return HttpResponse(f"<h1>DELETED {desc}</h1>")

#With a target ID
def genericDelete(MDL,id):
    targetLedger = get_SpecificLedgerID(MDL,id)
    desc = targetLedger.__str__()
    targetLedger.delete()
    return HttpResponse(f"<h1>ledger {desc} delete</h1>")

#error handling decorator 
def delete_Error_Decorator(func):
    def wrapper(request, *args, **kwargs):
        try: 
            result = func(request, *args, **kwargs)
            reBalance()
        except Exception as e: 
            result = HttpResponse("Deletion Error: " + str(e), status=500)
        return result
    return wrapper

def Error_Decorator(func):
    def wrapper(request, *args, **kwargs):
        try: 
            result = func(request, *args, **kwargs)
            reBalance()
        except Exception as e: 
            result = HttpResponse("General Error: " + str(e), status=500)
        return result
    return wrapper

def modifyBalance(MDLobj):
        currentID = MDLobj.id
        try:
            arrayPrevs = MDLobj.__class__.objects.filter(id__lt=currentID)
            prevObj = arrayPrevs.last()
            prevBalance =  prevObj.balance 

        except:
            prevBalance = 0
            MDLobj.balance = prevBalance

        netAmount = MDLobj.debit + MDLobj.credit 
        if MDLobj.id == 192:
            print(f"net amount {netAmount}")
            print(f"prevBalance {prevBalance}")
        MDLobj.balance = prevBalance + netAmount
        MDLobj.save()
        return MDLobj.balance


def balance(MDL):
    allEntries = MDL.objects.all()
    new_Balances  = []
    for item in allEntries :
        new_Balances.append(modifyBalance(item))
    return new_Balances  

def reBalance():
    getLedgersF(balance)
    


"""
the split will be able to handle any entry regardless if it was included 
in a entry split or just a single entry on it's own
"""
#Split decorator
@delete_Error_Decorator
def split_Decorator(func):
    def wrapper(MDL, id):
        try: 
            refLedger = MDL.objects.get(id=id)
            ledger_ID = refLedger.ledger_id
            userLedgers = getAppLedgers()
            func(Ledger, ledger_ID)
            for userLedger in userLedgers:
                #utilizing the ledger id of the intial query to collect each userledger's corresponding related obj
                if userLedger.objects.get(ledger_id=ledger_ID) != None:
                    userLedger_line = userLedger.objects.get(ledger_id=ledger_ID)
                    id =  userLedger_line.id    
                    func(userLedger, id)
                else:
                    pass
            
            return "split success"
        except Exception as e:
            print(e)
            return "split failed"
    reBalance()        
    return wrapper


