from django.core.management.base import BaseCommand
from django.conf import settings
from social.models import SocialAccount, SocialAccountType, TwitterAccount
from twython import Twython, TwythonError
from social.twitter.mapper import Mapper
from social.twitter.appliance import TwitterAppliance
from optparse import make_option

class Command(BaseCommand):
    help = ('''Gets all the twitter accounts associated with the active account types 
        in the system and populates the TwitterAccount table with the details associated with them''')
    
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
        
        print(TwitterAccount.objects.all())
        """
        Loop through each account and see if that account is set up and is valid. 
        if it comes back false mark the account as inactive and put a not on it.
        """
        
        if options['twitter_account_id'] == None:
            accounts = SocialAccount.objects.filter(account_type=1)
        else:
            print("Running with twitter account " + options['twitter_account_id'])
            accounts = SocialAccount.objects.filter(account_id=options['twitter_account_id'])
        
        for social_account in accounts:
            
            appliance = TwitterAppliance(social_account)
            twitter = appliance.get_twitter()
            
            try:
                profile = twitter.show_user(screen_name=social_account.username)
            except TwythonError as e:
                print e

            ta,created = TwitterAccount.objects.get_or_create(id=profile['id'])
            if(created):
                print("Created a new account holder for " + social_account.username)
            ta = Mapper.bindJson(profile,ta)
            ta.save()
            
            
            
