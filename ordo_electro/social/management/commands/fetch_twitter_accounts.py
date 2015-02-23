from django.core.management.base import BaseCommand
from django.conf import settings
from social.models import SocialAccount, SocialAccountType, TwitterAccount
from twython import Twython, TwythonError
from social.twitter.mapper import Mapper
import json

class Command(BaseCommand):
    help = ('''Gets all the twitter accounts associated with the active account types 
        in the system and populates the TwitterAccount table with the details associated with them''')
    
    def handle(self, *args, **options):
        
        print(TwitterAccount.objects.all())
        """
        Loop through each account and see if that account is set up and is valid. 
        if it comes back false mark the account as inactive and put a not on it.
        """
        for account in SocialAccount.objects.filter(account_type=1):
            
            if (account.secret == '' or account.token == ''):
                # maybe we should get the token now. 
                twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET)
                
                continue
            if (account.username == '' ): 
                raise Exception("Username is not set")
            
            print("Account: Oauth Token " + account.token + " Secret: " + account.secret)
            twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                              account.token,  account.secret)
            try:
                profile = twitter.show_user(screen_name=account.username)
            except TwythonError as e:
                print e


            ta,created = TwitterAccount.objects.get_or_create(twitter_id=profile['id'])
            if(created):
                print("Created a new account holder for " + account.username)
            ta = Mapper.bindJson(profile,ta)
            ta.save()
            
            
            
