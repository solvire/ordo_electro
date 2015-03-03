from django.conf import settings
from twython import Twython,TwythonError

'''
Created on Mar 3, 2015

@author: SS
'''

class TwitterAppliance:
    
    # the twython api interface 
    twitter = None
    social_account = None
    
    def __init__(self,social_account):

        self.social_account = social_account
        self.twitter = self.getTwitter()
        
    
    def getTwitter(self):
        if self.twitter == None:
            self.twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                           self.social_account.token,  self.social_account.secret)
        return self.twitter
    
    def getRates(self,resources=None):
        twitter = self.getTwitter()
        rates = twitter.get_application_rate_limit_status(resources=resources)
        return rates
        
    def isLimited(self,rates,resource,endpoint):
        vals = rates['resources'][resource][endpoint]
        if vals['remaining'] <= 1: return True
        
        print(str(vals['remaining']) + " hits left for " + resource)
        return False;
    
    def getLimits(self,twitter):
        twitter = self.getLimits()
        return True