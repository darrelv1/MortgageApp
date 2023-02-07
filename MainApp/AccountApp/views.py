from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .Controllers import ProfileController

from .models import Ledger, userLedger1, userLedger2, userLedger3, AppLedger, UserProfile
#Custome Built Serializers
from .serializers import (AccountSerializer
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



"""
********************************
ALL GET REQUESTS
********************************
"""




"""
********************************
    ALL DELETE REQUESTS
********************************
"""

"""GENERIC HELPERS"""

#plug-in pass through mutiple params 
def call_function(func, *args,):
        return func(*args)

#mini-func get target object
def get_SpecificLedgerID(MDL,id):
    return  MDL.objects.get(id = id)
        

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
        except Exception as e: 
            result = HttpResponse("Deletion Error: " + str(e), status=500)
        return result
    return wrapper

#Split decorator
@delete_Error_Decorator
def split_Decorator(func):
    def wrapper(MDL, id):
        try: 
            refLedger = MDL.objects.get(id=id)
            ledger_ID = refLedger.ledger_id
            userLedgers = getAppLedgers()
            # for userLedger in userLedgers:
            #     #utilizing the ledger id of the intial query to collect each userledger's corresponding related obj
            #     userLedger_line = userLedger.objects.get(ledger_id=ledger_ID)
            #     id =  userLedger_line.id    
            #     func(userLedger, id)
            func(Ledger, ledger_ID)
            return "split success"
        except Exception as e:
            print(e)
            return "split failed"
    return wrapper


"""LEDGER"""

#deletes all main LedgerEntries
@delete_Error_Decorator
def deleteALLledger(request):
    genericDeleteAll(Ledger)
    return HttpResponse("<h1>All Deleted</h1>")

#delete specific LedgerEntry
@delete_Error_Decorator
def deleteLedger(request, id):
    return genericDelete(Ledger,id)


"""ALL APPLEDGER SUBCLASSES"""

#deletes all Entries from AppLedger subclasses
@delete_Error_Decorator
def deleteALLsubclasses(request):
    getAppLedgersF(genericDeleteAll)
    return HttpResponse("<h1>All Deleted</h1>")

"""USERLEDGER1"""

#deletes all Entries from AppLedger subclasses
@delete_Error_Decorator
def deleteALL_userledger1(request):
    return genericDeleteAll(userLedger1)

#delete specific LedgerEntry
@delete_Error_Decorator
def delete_userledger1(request, id):
    return genericDelete(userLedger1,id)    

"""USERLEDGER2"""

#deletes all Entries from AppLedger subclasses
@delete_Error_Decorator
def deleteALL_userledger2(request):
    return genericDeleteAll(userLedger2)
    
#delete specific LedgerEntry
@delete_Error_Decorator
def delete_userledger2(request, id):
    return  genericDelete(userLedger2,id)

"""USERLEDGER3"""

#deletes all Entries from AppLedger subclasses
@delete_Error_Decorator
def deleteALL_userledger3(request):
    return genericDeleteAll(userLedger3)

#delete specific LedgerEntry
@delete_Error_Decorator
def delete_userledger3(request, id):
    return genericDelete(userLedger3,id)
    

#***SPLIT***

#subledger delete all affiliated entries from all ledgers
#alternative generic delete method
@split_Decorator
def genericDelete_alt(MDL, id):
    targetLedger = get_SpecificLedgerID(MDL,id)
    desc = targetLedger.__str__()
    targetLedger.delete()

def delete_split1(request, id):
    genericDelete_alt(userLedger1, id)
    return HttpResponse(f"<h1>deleted {id} </h1>")

def delete_split2(request, id):
    genericDelete_alt(userLedger2, id)
    return HttpResponse(f"<h1>deleted {id} </h1>")

def delete_split3(request, id):
    genericDelete_alt(userLedger3, id)
    return HttpResponse(f"<h1>deleted {id} </h1>")


"""
********************************
ALL CREATE REQUESTS
********************************
"""





"""
********************************
ALL UPDATE REQUESTS
********************************
"""




def delALLappledger(request):
    AppLedger.__subclasses__()
    a = [ e.objects.all().delete() for e in AppLedger.__subclasses__() ]
    return HttpResponse("<h1>All Deleted</h1>")

def delALLusers(request):
    UserProfile.objects.all().delete()
    return HttpResponse("<h1>All Deleted</h1>")
   

def getLastItem():
    lastitem = Ledger.objects.order_by('id').last()
    return lastitem

class LedgerView(generics.CreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = AccountSerializer

#Handles a Post Request to General Ledger
class CreateAccountView(APIView):
    
    serializer_class = CreateAccountSerializer
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        #serialize to python primitive type and see if the data sent was valid
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            date = serializer.data.get('date')
            amount = serializer.data.get('debit')
            description = serializer.data.get('description')

            queryset = Ledger.objects.filter(description="THis aa is the last item in the ledger")
            #queryset = Ledger.objects.filter(self.request.session.session_key)
            #Modifies if previous record exists
            if queryset.exists():
                ledger = queryset[0]
                ledger.date = date

                ledger.debit = (amount if amount > 0 else 0)
                ledger.credit = (amount if amount < 0 else 0)
                ledger.description = description
                ledger.save(update_fields=['date', 'debit', 'description'])
            #Creates new record
            else: 
                
                ledger = Ledger(date=date, debit=amount, description=description) if amount > 0 else Ledger(date=date, credit=amount, description=description)
                ledger.save()
                
       
            return Response(AccountSerializer(ledger).data,status=status.HTTP_202_ACCEPTED)

class DeleteAccountView(APIView):
    serializer_class = DeleteAccountSerializer
    
    def delete(self, request, id, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            print("Serializer is valid")
        print(id)
        #Will Get the item and then delete it
        ledger = Ledger.objects.get(id = id)
        ledger.delete()

        #Pulling a query of all the items in the ledger
        all_ledger = Ledger.objects.all()
        return Response(AccountSerializer(all_ledger, many=True).data,status=status.HTTP_201_CREATED)

class DeleteUserView(APIView):
    serializer_class = DeleteUserLedSerializer
    
    def delete(self, request, id, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            print("Serializer is valid")
        print(id)
        #Will Get the item and then delete it
        ledger = userLedger1.objects.all().delete()
        #ledger.delete()

        #Pulling a query of all the items in the ledger
        all_ledger = userLedger1.objects.all()
        return HttpResponse('<h1>All Deleted</h1>')
        #return Response(UserLedgerSerializer(all_ledger, many=True).data,status=status.HTTP_201_CREATED)


class UserLedgerPOST(APIView):
    serializer_class = CreateUserLedgerSerializer2 if userLedger1.objects.all().count() > 0 else CreateUserLedgerSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print("Serializer is valid")

        date = serializer.data.get('date')
        amount = serializer.data.get('amount')
        description = serializer.data.get('description')
        user = serializer.data.get('userName')
        rate = serializer.data.get('rate')

            
                
        #Main Ledger Instance
        tempLedger = Ledger(date=date, debit=amount, description=description) if amount > 0 else Ledger(date=date, credit=amount, description=description)  
        tempLedger.save()
            
            
        if not userLedger1.objects.exists():
            instUserPro = UserProfile(name=user, rate=rate)
            instUserPro.save()

        tempLine = userLedger1(date = date, 
                            debit = amount if amount > 0 else 0, 
                            credit = amount if amount < 0 else 0,
                            description = description,
                            ledger=tempLedger, 
                            user =  None if userLedger1.objects.exists() else instUserPro) 


        tempLine.save()
        
        allItems = userLedger1.objects.all()

        return Response(UserLedgerSerializer(allItems, many=True).data,status=status.HTTP_201_CREATED)


class UserLedgerPOST2(APIView):
    serializer_class = CreateUserLedgerSerializer2 if userLedger2.objects.all().count() > 0 else CreateUserLedgerSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print("Serializer is valid")

        date = serializer.data.get('date')
        amount = serializer.data.get('amount')
        description = serializer.data.get('description')
        user = serializer.data.get('userName')
        rate = serializer.data.get('rate')

            
                
        #Main Ledger Instance
        tempLedger = Ledger(date=date, debit=amount, description=description) if amount > 0 else Ledger(date=date, credit=amount, description=description)  
        tempLedger.save()
            
            
        if not userLedger2.objects.exists():
            instUserPro = UserProfile(name=user, rate=rate)
            instUserPro.save()

        tempLine = userLedger2(date = date, 
                            debit = amount if amount > 0 else 0, 
                            credit = amount if amount < 0 else 0,
                            description = description,
                            ledger=tempLedger, 
                            user =  None if userLedger2.objects.exists() else instUserPro) 

        
        tempLine.save()


        
        allItems = userLedger2.objects.all()

        return Response(UserLedgerSerializer(allItems, many=True).data,status=status.HTTP_201_CREATED)

class UserLedgerPOST3(APIView):
    serializer_class = CreateUserLedgerSerializer2 if userLedger3.objects.all().count() > 0 else CreateUserLedgerSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print("Serializer is valid")

        date = serializer.data.get('date')
        amount = serializer.data.get('amount')
        description = serializer.data.get('description')
        user = serializer.data.get('userName')
        rate = serializer.data.get('rate')

            
                
        #Main Ledger Instance
        tempLedger = Ledger(date=date, debit=amount, description=description) if amount > 0 else Ledger(date=date, credit=amount, description=description)  
        tempLedger.save()
            
            
        if not userLedger3.objects.exists():
            instUserPro = UserProfile(name=user, rate=rate)
            instUserPro.save()

        tempLine = userLedger3(date = date, 
                            debit = amount if amount > 0 else 0, 
                            credit = amount if amount < 0 else 0,
                            description = description,
                            ledger=tempLedger, 
                            user =  None if userLedger3.objects.exists() else instUserPro) 


        tempLine.save()
        
        allItems = userLedger3.objects.all()

        return Response(UserLedgerSerializer(allItems, many=True).data,status=status.HTTP_201_CREATED)


#Split the amount

class entrySplit(APIView):
    serialize_class = splitSerializer

    def post(self, request, format=None):

        serializer = self.serialize_class(data=request.data)

        if serializer.is_valid():
            
            

            date = serializer.data.get('date')
            amount = serializer.data.get('amount')
            description = serializer.data.get('description')

            subclasses = AppLedger.__subclasses__()
            output = subclasses[0].objects.first()
            mainledger = Ledger.objects.create(
                                                date=date,
                                                debit= amount if amount > 0 else 0,
                                                credit= amount if amount < 0 else 0,
                                                description=description
                                                )
            appLedgers = [ele for ele in subclasses]

            def rateExtractor(ele):
                userid = ele.objects.first().user.id
                userobj = UserProfile.objects.get(id=userid)
                print(f"userobj: {userobj}\n userobj-type: {type(userobj)}")
                
                rateamount = amount * userobj.rate
                print(f"rateamount: {rateamount}\n rateamount-type: {type(rateamount)}")

                return ele.objects.create(
                                    date=date
                                    ,debit=rateamount
                                    ,description=description
                                    ,ledger=mainledger
                                    )

            list(map(lambda eleLedger: rateExtractor(eleLedger), appLedgers))

        return Response(status=status.HTTP_201_CREATED)



def index(request):
    #result = ProfileController.createProfile("Darrel Valdivieso", 0.45)
    # lastitem = getLastItem()
    # print(lastitem.balance)
    # print(type(lastitem))
    # print("THIS IS WORKING")
    result = "The index page"
    # cal = lastitem.balance + 100
    # print (cal)
    Ledger.objects.create(date="2008-04-30",credit=0,   debit=350, description="THis is the last item in the ledger")
    return HttpResponse(f"<h1>{result}</h1>")



def entryPOST(request):
    if request.method == 'POST':
       amount = request.POST.get('amount')
       description = request.POST.get('description')
        # Do something with the data
       print("WORKIINNGGGGGGG!") 
       data = {'key': 'value'}
       response = JsonResponse(data)
       response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
       return response
    else:
        print(request.method)
        return JsonResponse({'status': 'error'})
    
#Debug & playaround
def tester2(request):
    subclasses = AppLedger.__subclasses__()
    output = subclasses[0].objects.first()
    amount = 1200
    mainledger = Ledger.objects.create(date="2008-08-29",debit=amount, description='Split Amount Testing')
    appLedgers = [ele for ele in subclasses ]

    def rateExtractor(ele):
        userid = ele.objects.first().user.id
        userobj = UserProfile.objects.get(id=userid)
        print(f"userobj: {userobj}\n userobj-type: {type(userobj)}")
        
        rateamount = amount * userobj.rate
        print(f"rateamount: {rateamount}\n rateamount-type: {type(rateamount)}")
        return ele.objects.create(date="2008-08-29", debit=rateamount, description="Split Amount Testing",ledger=mainledger )


    list(map(lambda eleLedger: rateExtractor(eleLedger), appLedgers))
    #print(f"output: {appLedgers[0]}\n output-type: {type(appLedgers[0])}")
    subclasses_list = [str(sc.user) for sc in subclasses]
    return JsonResponse(subclasses_list, safe=False)


def tester(request):
    ledger = Ledger.objects.get(id=135)
    print(ledger._meta.related_objects)
    INSuserledger1 = ledger.userledger1.all()
    INSuserledger2 = ledger.userledger2.all()   
    INSuserledger3 = ledger.userledger3.all()
    print(f'userledger1: {userLedger1}')
    print(f'userledger2: {userLedger2}')
    print(f'userledger3: {userLedger3}')
    
    return JsonResponse({"Hello": "hello"}, safe=False)
    


            