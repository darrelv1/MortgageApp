from rest_framework import serializers 
from .models import Ledger, userLedger1, userLedger2, userLedger3

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

class DeleteUserLedSerializer(serializers.ModelSerializer):
    class Meta:
        model = userLedger1
        fields = ['id',]

class CreateUserLedgerSerializer(serializers.Serializer):
    date = serializers.DateField(required=True)
    amount = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length = 100, required=True)
    userName = serializers.CharField(required=True)
    rate = serializers.FloatField(required=True)

class CreateUserLedgerSerializer2 (serializers.Serializer):
    date = serializers.DateField(required=True)
    amount = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length = 100, required=True)
    


    # class Meta:
    #   fields = ['data', 'amount', 'description', 'userName', 'rate']

class UserLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = userLedger1
        fields = '__all__'
