
from django.urls import path
from .views import index, entryPOST


urlpatterns = [
    path('Accounts/', index),
    path('Accounts_POST/', entryPOST)
    
]


