from social.models import Account, TwitterAccount, TwitterAccountRelationship, AccountType
from social.serializers import AccountSerializer, TwitterAccountSerializer, TwitterAccountRelationshipSerializer, AccountTypeSerializer
from django.shortcuts import get_object_or_404
from django.views.generic import View
from rest_framework import viewsets, generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def list(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AccountSerializer(user)
        return Response(serializer.data)
   

class AccountTypeViewSet(NestedViewSetMixin, ModelViewSet):
    model = Account   
   
class TwitterAccountViewSet(NestedViewSetMixin, ModelViewSet):
    model = TwitterAccount

class TwitterAccountRelationshipViewSet(NestedViewSetMixin, ModelViewSet):
    model = TwitterAccountRelationship
    

    
       
class AccountTypeList(generics.ListCreateAPIView):
    model = AccountType
    serializer_class = AccountTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class AccountTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = AccountType
    serializer_class = AccountTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    
"""
Twitter related social items 
TODO move these sub
"""
class TwitterAccountOverviewView(View):
    template_name = 'social/twitter.html'
#     form_class = UploadForm
    
class TwitterAccountList(generics.ListCreateAPIView):
    model = TwitterAccount
    serializer_class = TwitterAccountSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class TwitterAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    model = TwitterAccount
    serializer_class = TwitterAccountSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
        
class TwitterAccountRelationshipList(generics.ListCreateAPIView):
    model = TwitterAccountRelationship
    serializer_class = TwitterAccountRelationshipSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class TwitterAccountRelationshipDetail(generics.RetrieveUpdateDestroyAPIView):
    model = TwitterAccountRelationship
    serializer_class = TwitterAccountRelationshipSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    
class TwitterOverviewList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class TwitterOverviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.AllowAny
    ]