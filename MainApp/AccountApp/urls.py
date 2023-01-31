
from re import L
from django.urls import path
from .views import entryPOST, index, LedgerView, CreateAccountView, DeleteAccountView, UserLedgerPOST, tester, DeleteUserView


urlpatterns = [
    
    path('test',index),
    path('Accounts_POST/', entryPOST),
    path('Accounts_serial/', LedgerView.as_view()),
    path('create/', CreateAccountView.as_view()),
    
    path('delLedger/<int:id>', DeleteAccountView.as_view()),
    path('deluserLedger/<int:id>', DeleteUserView.as_view()),

    path('createU/', UserLedgerPOST.as_view()),
    path('tester/', tester)
    
]


