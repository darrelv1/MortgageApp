from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .Controllers import ProfileController

from .models import Ledger
from .serializers import AccountSerializer, CreateAccountSerializer


from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response



import json

class LedgerView(generics.CreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = AccountSerializer

class CreateAccountView(APIView):
    serializer_class = CreateAccountSerializer
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session.key):
            self.request.session.create()

        #serialize to python primitive type and see if the data sent was valid
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            date = serializer.data.date
            amount = serializer.data.debit
            description = serializer.data.description

            queryset = Ledger.objects.filter(self.request.session.session_key)
            if queryset.exists():
                ledger = queryset[0]
                ledger.date = date
                ledger.debit = amount
                ledger.description = description
                ledger.save(update_fields=['date', 'debit', 'description'])
            else: 
                ledger = Ledger(date=date, debit=amount, description=description)
                ledger.save()

            return Response(AccountSerializer(ledger).data,status=status.HTTP_202_ACCEPTED)


def index(request):
    result = ProfileController.createProfile("Darrel Valdivieso", 0.45)
    print("THIS IS WORKING")
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
    


    