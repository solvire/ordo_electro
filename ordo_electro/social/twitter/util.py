from django.conf import settings
from twython import Twython

import numpy as np
import datetime
import math

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
        
    def checkRate(self,rates,resource,endpoint):
        """
        See if the API is telling us to wait. 
        this can be called more than other calls so we should hit it with a little more frquency. 
        """
        vals = rates['resources'][resource][endpoint]
        if vals['remaining'] <= 1: return True
        
        print(str(vals['remaining']) + " hits left for " + resource)
        return False;
    
    def hitSystemHardLimit(self,social_account,endpoint):
        """
        If we have his the internal system limit. 
        This should probably be moved into another system but for now it's okay in here.
        This should be pulled from Redis since we can cache things up in there and not burdon other things
        
        Assumption: system clock is working and in sync with twitter's clock 
        
        algorithm:
            Check the hits against this user+resource 
            See if this user is about to hit X times in the last few minutes 
        """
        
    
    def getLimits(self,twitter):
        twitter = self.getLimits()
        return True
    
class TwitterRateThrottle():
    """
    Used to limit the hits to twitter
    Should be consulted before each call to twitter 
    Can check out internal redis or can call the twitter API 
    """
    
    def checkCache(self, social_account, endpoint):
        """
        KEY: social_account.id + hr_of_day + this_15min_window (integer) + endpoint 
        """
        now = datetime.datetime.now()
        key = str(social_account.id) + str(now.hour) + str(int(math.ceil(now.minute/15))) + endpoint
        
        
        
    

class TwitterRateMatrix():
    
    """
    The matrix as listed on the API docs site
    @see: https://dev.twitter.com/rest/public/rate-limits 
    ( METHOD, endpoint, family, user limit 15-min, app limit 15-min )
    """
    rates = np.array([
                ["GET","application/rate_limit_status","application",180,180],
                ["GET","favorites/list","favorites",15,15],
                ["GET","followers/ids","followers",15,15],
                ["GET","followers/list","followers",15,30],
                ["GET","friends/ids","friends",15,15],
                ["GET","friends/list","friends",15,30],
                ["GET","friendships/show","friendships",180,15],
                ["GET","help/configuration","help",15,15],
                ["GET","help/languages","help",15,15],
                ["GET","help/privacy","help",15,15],
                ["GET","help/tos","help",15,15],
                ["GET","lists/list","lists",15,15],
                ["GET","lists/members","lists",180,15],
                ["GET","lists/members/show","lists",15,15],
                ["GET","lists/memberships","lists",15,15],
                ["GET","lists/ownerships","lists",15,15],
                ["GET","lists/show","lists",15,15],
                ["GET","lists/statuses","lists",180,180],
                ["GET","lists/subscribers","lists",180,15],
                ["GET","lists/subscribers/show","lists",15,15],
                ["GET","lists/subscriptions","lists",15,15],
                ["GET","search/tweets","search",180,450],
                ["GET","statuses/lookup","statuses",180,60],
                ["GET","statuses/oembed","statuses",180,180],
                ["GET","statuses/retweeters/ids","statuses",15,60],
                ["GET","statuses/retweets/:id","statuses",15,60],
                ["GET","statuses/show/:id","statuses",180,180],
                ["GET","statuses/user_timeline","statuses",180,300],
                ["GET","trends/available","trends",15,15],
                ["GET","trends/closest","trends",15,15],
                ["GET","trends/place","trends",15,15],
                ["GET","users/lookup","users",180,60],
                ["GET","users/show","users",180,180],
                ["GET","users/suggestions","users",15,15],
                ["GET","users/suggestions/:slug","users",15,15],
                ["GET","users/suggestions/:slug/members","users",15,15]
            ])
    
    def getRateForEndpoint(self, endpoint=None):
        
        if endpoint == None:
            raise InvalidTwitterEndpointException(endpoint, "Provide an endpoint")
        if endpoint != None and not self.isValidEndpoint(endpoint):
            raise InvalidTwitterEndpointException(endpoint, "The endpoint " + str(endpoint) + " is invalid ")
        
        # loop them and if we find the endpoint key send the limit value 
        for rate in self.rates:
            if endpoint in rate:
                return rate[3]
            
        # if we don't find it set default to 15 
        return 15
            
    
    def isValidEndpoint(self, endpoint):
        """Exact match to the 2nd column"""
        return endpoint in self.rates[:,1]
    
    
        
class TwitterApplianceException(Exception):
    """
    Base exception 
    """
    pass

class InvalidTwitterEndpointException(TwitterApplianceException):
    """
    Exception raised by looking for invalid resources

    Attributes:
        endpoint -- the endpoint looked for
        msg  -- explanation of the error
    """
    def __init__(self, endpoint, msg):
        # string data about the exception 
        self.endpoint = endpoint
        self.msg = msg
    