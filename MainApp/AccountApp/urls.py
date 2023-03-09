
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
                   delALLusers,
                   delete_userledger1,
                   delete_userledger2,
                   delete_userledger3,
                   delete_split1,
                   delete_split2,
                   delete_split3,
                   getLedgerAll,
                   getLedgerby_id,
                   getLedgersby_Name,
                   getAll_userLedgers,
                   getUserProfilesby_Name,
                   createLedger,
                   inProgress,
            
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

    path('deleteUL1/<int:id>', delete_userledger1),
    path('deleteUL2/<int:id>', delete_userledger2),
    path('deleteUL3/<int:id>', delete_userledger3),
    path('deleteSplit1/<int:id>', delete_split1),
    path('deleteSplit2/<int:id>', delete_split2),
    path('deleteSplit3/<int:id>', delete_split3),

    path('createU/', UserLedgerPOST.as_view()),
    path('createU2/', UserLedgerPOST2.as_view()),
    path('createU3/', UserLedgerPOST3.as_view()),


    path('split/', entrySplit.as_view()),

    path('qwerty/', createLedger.as_view()),
    path('inProgress/', tester),
    
    path('getLedgerAll', getLedgerAll.as_view()),
    path('getLedger/<str:id>', getLedgerby_id.as_view()),
    path('getLedgerByName/<str:string>', getLedgersby_Name.as_view()),
    path('getAllul', getAll_userLedgers.as_view()),
    path('getUserNames',getUserProfilesby_Name.as_view()) 
]


