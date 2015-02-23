'''
Created on Feb 22, 2015

@author: SS
'''
from django.core.management.base import BaseCommand
from social.models import SocialAccount, TwitterAccountRelationship, TwitterAccount
from optparse import make_option
import json

from social.twitter.relationship import RelationshipUtils

class Command(BaseCommand):
    help = ('''Get all the relationships for the accounts stored in the system. 
    Example: social_accounts/1/twitter/followers 
    It can take parameters so that you can specify only the related accounts that you want to approach  
    It will take any twitter account and find relationships for it
    If no accounts are suggested then it will just loop through the social accounts (not recommended)
    ''')
    
    option_list = BaseCommand.option_list + (
        make_option(
            "-a", 
            "--twitter_account_id", 
            dest = "twitter_account_id",
            help = "The account to find relationships for", 
            metavar = "ACCOUNTID"
        ),
    )

    
    def handle(self, *args, **options):
        """
        Loop through each account and see if that account is set up and is valid. 
        if it comes back false mark the account as inactive and put a not on it.
        """
        # loop all of them then
        if options['twitter_account_id'] == None:
            for social_account in SocialAccount.objects.filter():
                print("Saving followers for: " + social_account.username)
                twitter_account = TwitterAccount.objects.get(twitter_id=social_account.account_id)
                followers = RelationshipUtils.fetch_followers(social_account)
                RelationshipUtils.save_followers(followers, twitter_account)
