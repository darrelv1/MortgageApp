from django.shortcuts import render
from django.http import HttpResponse
from .Main import *


def index(request):
    add()
    return HttpResponse(f"<h1>Accounting App</h1>")
