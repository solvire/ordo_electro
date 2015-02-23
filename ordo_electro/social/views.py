from social.models import SocialAccount, TwitterAccount, TwitterAccountRelationship, SocialAccountType
from social.serializers import SocialAccountSerializer, TwitterAccountSerializer, TwitterAccountRelationshipSerializer, SocialAccountTypeSerializer, TwitterAccountFollowerSerializer
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_extensions.decorators import link

from social.twitter.mapper import Mapper
from social.twitter.relationship import RelationshipUtils

from twython import Twython, TwythonError
import json


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
    social_account = SocialAccount.objects.get(id=request.session['social_account_id'])
    
    # let's update some values for the main social account that we have     
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
    # i know this is redundant saves but if we failed after trying twython 
    # i didn't want to lose the secret and teh keys up there. 
    social_account.account_id = profile['id']
    social_account.save() 
    
    return redirect('/#/twitter/accounts')

class SocialAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountSerializer
    
    def list(self, request):
        queryset = SocialAccount.objects.all()
        serializer = SocialAccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SocialAccount.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SocialAccountSerializer(user)
        return Response(serializer.data)
   

class SocialAccountTypeViewSet(NestedViewSetMixin, ModelViewSet):
    model = SocialAccount   
   
class TwitterAccountViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = TwitterAccountSerializer
    model = TwitterAccount
    queryset = TwitterAccount.objects.all()
    
    
    def list(self, request):
        
        # get the list of new users loaded in if necessary 
        
        queryset = TwitterAccount.objects.all()
        serializer = TwitterAccountSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        queryset = TwitterAccount.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TwitterAccountSerializer(user)
        return Response(serializer.data)


class TwitterAccountRelationshipViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = TwitterAccountRelationshipSerializer
    model = TwitterAccountRelationship
    queryset = TwitterAccountRelationship.objects.all()
    
    
    def list(self, request,parent_lookup_account):
        """
        this is probably a good place to check to see if the account needs to be refreshed 
        since we already have the parent account passed in we can check the last updated time for 
        friends and followers call update to it
        if 
        """
        social_account = SocialAccount.objects.get(id=parent_lookup_account)
        subject = TwitterAccount.objects.get(twitter_id=social_account.account_id)
        
        # get the followers and save all their profiles for later use 
#         followers = RelationshipUtils.fetch_followers(social_account, social_account.username)
        followers = json.load(open('/Users/moz/Desktop/data.json'))
        RelationshipUtils.save_followers(followers, subject)
        
        
        queryset = TwitterAccountRelationship.objects.filter(subject_id=subject.id)
        serializer = TwitterAccountRelationshipSerializer(queryset, many=True)
        
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        queryset = TwitterAccountRelationship.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TwitterAccountSerializer(user)
        return Response(serializer.data)
    
class TwitterAccountFollowerViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = TwitterAccountFollowerSerializer
    model = TwitterAccountRelationship
    
    
    def list(self, request,parent_lookup_account):
        """
        @see: TwitterAccountRelationshipViewSet.list 
        """
        social_account = SocialAccount.objects.get(id=parent_lookup_account)
        subject = TwitterAccount.objects.get(twitter_id=social_account.account_id)
        
        # get the followers and save all their profiles for later use 
        followers = RelationshipUtils.fetch_followers(social_account, social_account.username)
#         followers = json.load(open('/Users/moz/Desktop/data.json'))
        RelationshipUtils.save_followers(followers, subject)
        
        
        queryset = TwitterAccountRelationship.objects.filter(subject_id=subject.id)
#         pobject = [i.__dict__ for i in queryset]
#         print(pobject) 
        serializer = TwitterAccountFollowerSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    
    
class TwitterAccountFriendViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = TwitterAccountSerializer
    model = TwitterAccount
    
    
    def list(self, request,parent_lookup_account):
        """
        @see: TwitterAccountRelationshipViewSet.list 
        """
        social_account = SocialAccount.objects.get(id=parent_lookup_account)
        subject = TwitterAccount.objects.get(twitter_id=social_account.account_id)
        
        friends = TwitterAccountRelationship.objects.filter(subject=subject.twitter_account)
        serializer = TwitterAccountFollowerSerializer(friends, many=True)
        
        return Response(serializer.data)
        
       
class SocialAccountTypeList(generics.ListCreateAPIView):
    model = SocialAccountType
    serializer_class = SocialAccountTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class SocialAccountTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = SocialAccountType
    serializer_class = SocialAccountTypeSerializer
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