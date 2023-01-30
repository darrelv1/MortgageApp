from rest_framework import serializers 
from .models import Ledger


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('id', 'date', 'debit', 'credit',
                'balance', 'description')

#To serialize request incoming - only necessary fields 
class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('date', 'debit', 'description')

class DeleteAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id',]
