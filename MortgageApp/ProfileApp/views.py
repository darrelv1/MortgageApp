from django.shortcuts import render
from django.http import HttpResponse


def users(request):
    return HttpResponse("""<h1>Landing Page</h1>
                            <p>Where all the user will run CRUD ops </p>
                            """)
# Create your views here.
