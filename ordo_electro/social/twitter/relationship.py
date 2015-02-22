from django.conf import settings
from twython import Twython,TwythonError
from social.models import TwitterAccount
from mapper import Mapper

'''
Created on Feb 21, 2015

@author: SS
'''

class RelationshipUtils():

    @staticmethod
    def fetch_followers(self,social_account,subject_account):
        """
        Default action is to not store them here once we have them
        Later we can flag this if we don't want to create records for them
        it isn't that hard to pass this list to the save followers function 
        """
        if (social_account.secret == '' or social_account.token == ''):
            # maybe we should get the token now. 
            raise Exception("The secret or token are not set");
            
        if (social_account.username == '' ): 
            raise Exception("Username is not set")
        
        twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                          social_account.token,  social_account.secret)
        return twitter.get_followers_list(screen_name=social_account.username)
        
        
        
        
    def save_followers(self,followers):
        for follower in followers:
            ta,created = TwitterAccount.objects.get_or_create(twitter_id=follower['id'])
            if(created):
                print("Created a new account holder for " + follower['username'])
            ta = Mapper.bindJson(follower,ta)
            ta.save()
            
            