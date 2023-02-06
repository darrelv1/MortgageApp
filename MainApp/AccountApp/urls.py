
from re import L
from django.urls import path
from .views import (
                   entryPOST, 
                   index,
                   LedgerView,
                   CreateAccountView,
                   entrySplit,
                   DeleteAccountView, 
                   UserLedgerPOST, 
                   UserLedgerPOST2, 
                   UserLedgerPOST3, 
                   tester, 
                   DeleteUserView, 
                   delALLappledger, 
                   delALLusers
)


urlpatterns = [
    
    path('test',index),
    path('Accounts_POST/', entryPOST),
    path('Accounts_serial/', LedgerView.as_view()),
    path('create/', CreateAccountView.as_view()),
    
    path('delLedger/<int:id>', DeleteAccountView.as_view()),
    path('deluserLedger/<int:id>', DeleteUserView.as_view()),
    path('delappLedgers/',delALLappledger),
    path('delusers/', delALLusers),

    path('createU/', UserLedgerPOST.as_view()),
    path('createU2/', UserLedgerPOST2.as_view()),
    path('createU3/', UserLedgerPOST3.as_view()),

    path('tester/', tester),
    path('split/', entrySplit.as_view())
    
]


