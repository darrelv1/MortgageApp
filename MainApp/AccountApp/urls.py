
from re import L
from django.urls import path
from .views import entryPOST, index, LedgerView, CreateAccountView


urlpatterns = [
  
    path('Accounts_POST/', entryPOST),
    path('Accounts_serial/', LedgerView.as_view()),
    path('Accounts_create/', CreateAccountView.as_view())
    
]


