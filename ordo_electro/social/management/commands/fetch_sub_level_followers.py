'''
Created on Mar 3, 2015

@author: SS
'''
from django.core.management.base import BaseCommand, CommandError
from social.models import SocialAccount, TwitterAccount
from optparse import make_option
from datetime import timedelta
import time
from django.utils import timezone

from social.twitter.relationship import RelationshipUtils
from social.twitter.appliance import TwitterAppliance

class Command(BaseCommand):
    help = ('''Get all the followers for all these users' followers. It is a bit of a recursive crawl. 
    For right now it is very unsophisticated. It just crawls the crawl. 
    ''')
    
    option_list = BaseCommand.option_list + (
        make_option(
            "-a", 
            "--twitter_account_id", 
            dest = "twitter_account_id",
            help = "The account to find sub relationships for. Top level", 
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
            raise CommandError("You must provide a twitter account id to start with. This is the top level.")
        else:
            print("Running with twitter account " + options['twitter_account_id'])
            social_account = SocialAccount.objects.get(account_id=options['twitter_account_id'])
            
        print("Saving followers for: " + social_account.username)
        twitter_account = TwitterAccount.objects.get(id=social_account.account_id)
        
        appliance = TwitterAppliance(social_account)
        
        # if its more than a 1/2 day old run it again 
        if(twitter_account.followers_updated < timezone.now() - timedelta(hours=12) ):
            followers = RelationshipUtils.fetch_followers(social_account)
            RelationshipUtils.save_followers(followers, twitter_account, appliance)
            twitter_account.followers_updated = timezone.now()
            twitter_account.save()
        
        # now loop their followers 
        # start with the smallest followers
        self.sub_follow(social_account,twitter_account)

    def sub_follow(self,social_account,twitter_account):

#         accounts = TwitterAccount.objects.raw('''select a.* from 
#                 social_twitteraccount a,
#                 social_twitter_account_relationship r 
#                 WHERE
#                 a.id = r.target_id and 
#                 r.subject_id = 2723221604 and 
#                 followers_count BETWEEN 5 AND 25000
#                 ORDER BY followers_count ASC''')
        
        accounts = TwitterAccount.objects.raw('''select a.* from 
                social_twitteraccount a,
                social_twitter_account_relationship r 
                WHERE
                a.id = r.target_id and 
                r.subject_id = %s and 
                followers_count BETWEEN 5 AND 25000 AND 
                followers_updated < DATE_SUB(NOW(),INTERVAL 1 DAY)
                ORDER BY followers_count ASC''', [twitter_account.id])
        
        for account in accounts:
            print("Mining followers of: " + account.screen_name + " with " + str(account.followers_count) + " followers ")
            
            
            # check the rate limit here. 
            appliance = TwitterAppliance(social_account)
            
            while appliance.hit_system_hard_limit('followers/list'):
                resets_in = appliance.clock_resets_in('followers/list') + 60
                print("Resting " + resets_in)
                time.sleep(resets_in)
                
            peons = RelationshipUtils.fetch_followers(social_account,account.screen_name)
            RelationshipUtils.save_followers(peons, account, appliance)
            time.sleep(60)
        