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


#UserLedger1, userLedger2, userLedger3
# class UserLedgersSerializer(serializers.ModelSerializer):

#     date =serializers.DateField(required=True)
#     debit = serializers.IntegerField(required=True, default=0)
#     credit = serializers.IntegerField(required=True, default=0)
#     balance = serializers.IntegerField(required=True)
#     description = serializers.CharField(required=True, max_length = 150)
#     user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    
#     def create(self, validated_data):
#         """ Create and return a new ledger instance"""
#         model_class = self.context.get('model_class')
#         inst_ledger = model_class(
#             date=validated_data.get('date'), 
#             debit=validated_data.get('debit'),
#             credits=validated_data.get('credit'),
#             balance=validated_data.get('balance'),
#             description=validated_data.get('description'),
#             user=validated_data.get('user')
#         )
#         inst_ledger.save()
#         return inst_ledger 

#     def update(self, instance, validated_data):

#         instance.date = validated_data.get('date', instance.date)
#         instance.debit = validated_data.get('debit', instance.debit)
#         instance.credit = validated_data.get('credit', instance.credit)
#         instance.balance = validated_data.get('balance', instance.balance)
#         instance.description = validated_data.get('description', instance.description)
#         instance.user = validated_data.get('user', instance.user)
#         instance.save()
#         return instance 








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
