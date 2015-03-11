from social.models import TwitterAccount, TwitterAccountRelationship
from mapper import Mapper
from social.utils import Utils
from social.twitter.appliance import TwitterAppliance
from social.twitter.models import TwitterStatus

import time

'''
Created on Feb 21, 2015

@author: SS
'''

class RelationshipUtils():
    
    follower_pull_count = 200

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
        
        appliance = TwitterAppliance(social_account)
        twitter = appliance.get_twitter()
#         followers = twitter.get_followers_list(screen_name=screen_name,count=200)
        
        followers = twitter.cursor(twitter.get_followers_list, screen_name=screen_name,count=RelationshipUtils.follower_pull_count)
        
#         print(json.dumps(followers))
        return followers
        
    @staticmethod
    def save_followers(followers, subject, appliance, rate_limit=True):
        """
        Takes in a generator of followers to loop through. 
        check out the documentation on the followers list from twitter for the form. 
        
        second parameter is a TwitterAccount object to assign the followers to
        """
        count = 0
        for follower in followers:
            count += 1

            # then check to see if this profile account was created 
            ta,created = TwitterAccount.objects.get_or_create(id=follower['id'])
            if(created):
                print("Created a new account holder for " + follower['name'])
            ta = Mapper.bindJson(follower,ta)
            # should we be careful hitting all their links... probably no throttle limit
            if ta.url is not None:
                try:
                    url = Utils.unshorten_url(ta.url)
                except Exception: 
                    pass
                # keep it from being too long 
                if(url > 100):
                    url = url[:99] 
                ta.url = url
            
            try:
                ta.save()
            except Exception, e:
                print("Failure to save record " + str(e))
                continue
            
            # create the relationship 
            tar, created = TwitterAccountRelationship.objects.get_or_create(subject=subject, target=ta)
            tar.active = True
            tar.save()
            if(created):
                print("Created an account relationship between " + subject.name + " AND " + ta.name + " id: " + str( ta.id))
                
        
            # Get the status and save it if it doesn't exist 
            if 'status' in follower: 
                status, status_created = TwitterStatus.objects.get_or_create(status_id=follower['status']['id'])
#                 if status.status_id:
#                     print("Found a status of " + str(status.status_id) + " was created: " + str(status_created))
                status.twitter_id = ta.id
                status.status = follower['status']
                status.save()
        
            # check the rate limits again if we hit 200 calls 
            if rate_limit:
                if count >= RelationshipUtils.follower_pull_count:
                    count = 0
                    # TODO not the best place for this. It needs to be in the appliance where the calls should go through 
                    # TODO also we need to not use strings randomly and have keys for these endpoints 
                    appliance.increment_endpoint_count('followers/list')
                    
                # don't sync this with twitter... we hit it too much 
                while appliance.hit_system_hard_limit('followers/list'):
                    resets_in = appliance.clock_resets_in('followers/list') * 60 + 60
                    print("Resting save " + str(resets_in))
                    time.sleep(resets_in)
                    