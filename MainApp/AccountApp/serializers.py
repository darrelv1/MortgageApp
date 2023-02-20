from rest_framework import serializers 
from .models import Ledger, userLedger1, userLedger2, userLedger3, UserProfile
#CRUD plugins:

"""
********************************
ALL LEDGER SERIALIZERS
********************************
"""

"""RESPONSE SERIALIZERS"""

class Ledger_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'


#To serialize request incoming - only necessary fields 
class CreateLedgerSerializer(serializers.ModelSerializer):
    #Entry Form
    amount = serializers.IntegerField()
    
    class Meta:
        model = Ledger
        fields = ('date', 'description', 'amount')
    
    def create(self, validated_data):
        print(validated_data)
        instance = Ledger.objects.create(
            date = validated_data['date'],
            description = validated_data['description'], 
            debit = validated_data['amount'] if validated_data['amount'] > 0  else 0,
            credit = validated_data['amount'] if validated_data['amount'] < 0 else 0
        )
        instance.set_balance_Instance()
    
        return instance


class userLedgers_Serializer(serializers.Serializer):
    date = serializers.DateField(required=False)
    amount = serializers.IntegerField()
    balance = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False, max_length=150)
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    ledger = serializers.PrimaryKeyRelatedField(queryset=Ledger.objects.all())

    def __init__(self, *args, **kwargs):
        for key in kwargs.keys():
            print(f"key:{key}")
        
        self.model_class = kwargs.pop('model_class', None) 
        try:
            self.request = kwargs.get('context').get('request')
            self.HTTPMETHOD = self.request.method
            print(f"HTTP METHOD : {self.HTTPMETHOD}")
            if self.HTTPMETHOD == 'POST':
                self.fields.pop("balance")
                # self.fields.pop("user")
                self.fields.pop("ledger")
        except:
            print("didn't have a context parameter")
        super().__init__(*args, **kwargs)

    

    def create(self, validated_data):
        
        ledger = self.model_class(
            date=validated_data.get('date'),
            debit = validated_data['amount'] if validated_data['amount'] > 0  else 0,
            credit = validated_data['amount'] if validated_data['amount'] < 0 else 0,
            # balance=validated_data.get('balance'),
            description=validated_data.get('description'),
            user=validated_data.get('user'),
        )
        ledger.save()
        return ledger

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.debit = validated_data.get('debit', instance.debit)
        instance.credit = validated_data.get('credit', instance.credit)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.description = validated_data.get('description', instance.description)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance



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


#To delete from Ledger
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
    description = serializers.CharField(max_length = 150, required=True)
    userName = serializers.CharField(required=True)
    rate = serializers.FloatField(required=True)

class CreateUserLedgerSerializer2 (serializers.Serializer):
    date = serializers.DateField(required=True)
    amount = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length = 150, required=True)

class splitSerializer(serializers.Serializer):
    date = serializers.DateField(required=True)
    amount = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length = 150, required=True)
    
    # class Meta:
    #   fields = ['data', 'amount', 'description', 'userName', 'rate']

class UserLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = userLedger1
        fields = '__all__'
