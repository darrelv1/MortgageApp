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
                        )
#Django provide serializers
from django.core.serializers import serialize

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response



import json


def delALLledger(request):
    Ledger.objects.all().delete()
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


#Split the amount





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
def tester(request):
    subclasses = AppLedger.__subclasses__()
    output = subclasses[0].objects.first()
    
    print(f"output: {output}\n output-type: {type(output)}")
    subclasses_list = [str(sc.user) for sc in subclasses]
    return JsonResponse(subclasses_list, safe=False)