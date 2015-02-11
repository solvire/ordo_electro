from social.models import Account, TwitterAccount, TwitterAccountLink, AccountType
from social.serializers import AccountSerializer, TwitterAccountSerializer, TwitterAccountLinkSerializer, AccountTypeSerializer
from django.shortcuts import get_object_or_404
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

class TwitterAccountLinkViewSet(NestedViewSetMixin, ModelViewSet):
    model = TwitterAccountLink    
    
       
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
    
        
class TwitterAccountLinkList(generics.ListCreateAPIView):
    model = TwitterAccountLink
    serializer_class = TwitterAccountLinkSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class TwitterAccountLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    model = TwitterAccountLink
    serializer_class = TwitterAccountLinkSerializer
    permission_classes = [
        permissions.AllowAny
    ]