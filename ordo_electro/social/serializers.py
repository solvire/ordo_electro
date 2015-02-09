'''
Created on Feb 4, 2015

@author: solvire
'''
from django.forms import widgets
from rest_framework import serializers
from social.models import Account, AccountType
from datetime import datetime   


class AccountSerializer(serializers.Serializer):
    owner_id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    account_type = serializers.StringRelatedField()
    active = serializers.BooleanField(default=True)
    token = serializers.CharField(max_length=128)
    secret = serializers.CharField(max_length=128)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    
    def create(self, validated_data):
        """
        Create and return a new `Account` instance, given the validated data.
        """
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Account` instance, given the validated data.
        """
        instance.active = validated_data.get('active', instance.active)
        instance.token = validated_data.get('token', instance.token)
        instance.secret = validated_data.get('secret', instance.secret)
        instance.updated = datetime.now()
        instance.save()
        return instance
    
class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ('name','active')
        
        