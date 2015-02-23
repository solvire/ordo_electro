'''
Created on Feb 4, 2015

@author: solvire
'''
from rest_framework import serializers
from social.models import SocialAccount, SocialAccountType, TwitterAccount, TwitterAccountRelationship
from datetime import datetime   


class SocialAccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    owner_id = serializers.IntegerField()
    account_id = serializers.IntegerField()
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
        return SocialAccount.objects.create(**validated_data)

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
    
class SocialAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccountType
        fields = ('name','active')
        
        
class TwitterAccountSerializer(serializers.ModelSerializer):
    twitter_id = serializers.IntegerField()
    name = serializers.CharField()
    screen_name = serializers.CharField()
    location = serializers.CharField()
#     followers = serializers.HyperlinkedRelatedField(
#             many=True,
#             read_only=True,
#             view_name='track-detail'
#         )
    
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
    
    class Meta:
        model = TwitterAccount
        
class TwitterAccountFollowerSerializer(serializers.ModelSerializer):
    account = TwitterAccountSerializer(many=True, read_only=True)
    class Meta:
        model = TwitterAccountRelationship
        
    
        
class TwitterAccountRelationshipSerializer(serializers.ModelSerializer):
    subject = TwitterAccountSerializer(many=True)
    target = TwitterAccountSerializer(many=True)
    class Meta:
        model = TwitterAccountRelationship
        
        