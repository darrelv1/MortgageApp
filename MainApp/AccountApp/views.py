from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .Controllers import ProfileController

from .models import Ledger
from .serializers import AccountSerializer, CreateAccountSerializer, DeleteAccountSerializer


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
                print(serializer.data.get('debit'))
       
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
    


    