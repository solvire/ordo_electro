# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, viewsets

# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username
    class Meta:
        ordering = ['username']
    
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined')
        
        
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
