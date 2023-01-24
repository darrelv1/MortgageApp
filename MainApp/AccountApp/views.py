from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .Controllers import ProfileController




import json


def index(request):
    result = ProfileController.createProfile("Darrel Valdivieso", 0.45)
    print("THIS IS WORKING")
    return HttpResponse(f"<h1>{result}</h1>")

#cors_exempt
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
    
    