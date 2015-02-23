from django.conf import settings
from twython import Twython,TwythonError
from social.models import TwitterAccount, TwitterAccountRelationship
from mapper import Mapper
import json

'''
Created on Feb 21, 2015

@author: SS
'''

class RelationshipUtils():

    @staticmethod
    def fetch_followers(social_account, screen_name=None, cursor=None):
        """
        Args are gor 
        Default action is to not store them here once we have them
        Later we can flag this if we don't want to create records for them
        it isn't that hard to pass this list to the save followers function 
        """
        if (social_account.secret == '' or social_account.token == ''):
            # maybe we should get the token now. 
            raise Exception("The secret or token are not set");
        
        if(screen_name is None):
            screen_name = social_account.username
        
        if (screen_name == '' ): 
            raise Exception("screen_name is not set")
        
        twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                          social_account.token,  social_account.secret)
#         followers = twitter.get_followers_list(screen_name=screen_name,count=200)
        
        followers = twitter.cursor(twitter.get_followers_list, screen_name=screen_name,count=200)
        
#         print(json.dumps(followers))
        return followers
        
    @staticmethod
    def save_followers(followers, subject):
        """
        Takes in a generator of followers to loop through. 
        check out the documentation on the followers list from twitter for the form. 
        
        second parameter is a TwitterAccount object to assign the followers to
        """
        
        for follower in followers:

            # then check to see if this profile account was created 
            ta,created = TwitterAccount.objects.get_or_create(twitter_id=follower['id'])
            if(created):
                print("Created a new account holder for " + follower['name'])
            ta = Mapper.bindJson(follower,ta)
            ta.save()
            
            # create the relationship 
            tar, created = TwitterAccountRelationship.objects.get_or_create(subject=subject, target=ta)
            tar.active = True
            tar.save()
            if(created):
                print("Created an account relationship between " + subject.name + " AND " + ta.name)
            
            