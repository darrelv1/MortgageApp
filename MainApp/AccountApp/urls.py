
from re import L
from django.urls import path
from .views import entryPOST, index, LedgerView, CreateAccountView, DeleteAccountView


urlpatterns = [
    
    path('test',index),
    path('Accounts_POST/', entryPOST),
    path('Accounts_serial/', LedgerView.as_view()),
    path('create/', CreateAccountView.as_view()),
    path('delLedger/<int:id>', DeleteAccountView.as_view()),
    
]


