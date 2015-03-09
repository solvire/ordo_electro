'''
Created on Mar 8, 2015

@author: SS
'''
from django.core.management.base import BaseCommand
from social.models import SocialAccount
from optparse import make_option
from social.twitter.appliance import TwitterAppliance


class Command(BaseCommand):
    help = ('''Load (optionally save) the twitter timeline going back N records''')
    
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
        Get the timeline for this account. 
        Not really doing anything with it yet 
        """
        if options['twitter_account_id'] == None:
            raise Exception
        
        # loop all of them then
        print("Running with twitter account " + options['twitter_account_id'])
        social_account = SocialAccount.objects.get(account_id=options['twitter_account_id'])
        
        appliance = TwitterAppliance(social_account)
        twitter = appliance.get_twitter()
        timeline = twitter.get_user_timeline()
        
        print(timeline)
        
