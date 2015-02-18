from social.models import Account, TwitterAccount, TwitterAccountRelationship, AccountType
from social.serializers import AccountSerializer, TwitterAccountSerializer, TwitterAccountRelationshipSerializer, AccountTypeSerializer
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from social.twitter.mapper import Mapper

from twython import Twython, TwythonError


def oauth_redirect(request,social_account_id):
    
    if (not social_account_id.isdigit()): raise Exception("You must pass an integer " + social_account_id)
    
    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET)
    auth = twitter.get_authentication_tokens(callback_url='http://localhost:8000/social/twitter_oauth_verify/') #callback_url='http://eo.ordo.club/social/twitter_oauth'
    
    request.session['social_account_id'] = social_account_id
    request.session['OAUTH_TOKEN'] = auth['oauth_token']
    request.session['OAUTH_TOKEN_SECRET'] = auth['oauth_token_secret']
    
    return redirect(auth['auth_url'])

def oauth_verify(request):
    
    oauth_verifier = request.GET['oauth_verifier']
    
    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                      request.session['OAUTH_TOKEN'], request.session['OAUTH_TOKEN_SECRET'])
    final_tokens = twitter.get_authorized_tokens(oauth_verifier)
    
    OAUTH_TOKEN = final_tokens['oauth_token']
    OAUTH_TOKEN_SECRET = final_tokens['oauth_token_secret']
    
    
    # get the social account set up that we are going to tie this thing to 
    social_account = Account.objects.get(id=request.session['social_account_id'])
    
    
    social_account.token = OAUTH_TOKEN
    social_account.secret = OAUTH_TOKEN_SECRET
    social_account.save()
    
    
    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    # let's see if this worked     
    try:
        profile = twitter.show_user(screen_name=social_account.username)
    except TwythonError as e:
        print e
    
    # look up the record or create it if it doesn't exist 
    twitter_account, created = TwitterAccount.objects.get_or_create(twitter_id=profile['id'])
    
    print('An account was updated for ' + str(profile['id']) + ' user: ' + profile['screen_name'])
    
    # store the new keys we have for this one
    twitter_account = Mapper.bindJson(profile,twitter_account)
    twitter_account.save()
    
    # lets make sure the master social account associated 
    # with this object is created and in place 
    
    print(twitter_account)
    
    return redirect('/#/twitter/accounts')

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
    serializer_class = TwitterAccountSerializer
    model = TwitterAccount
    queryset = TwitterAccount.objects.all()
    
    
    def list(self, request):
        queryset = TwitterAccount.objects.all()
        serializer = TwitterAccountSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        queryset = TwitterAccount.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TwitterAccountSerializer(user)
        return Response(serializer.data)


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