from django.db import models
from django.utils.translation import ugettext_lazy as _

class SocialAccount(models.Model):
    owner_id = models.IntegerField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32, default='')
    account_id = models.BigIntegerField(default=0)
    account_type = models.ForeignKey('SocialAccountType')
    active = models.BooleanField(default=True)
    token = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ('created',)
        
class SocialAccountType(models.Model):
    name = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    
class TwitterAccountRelationship(models.Model):
    """
    A follower/follow/relation list basically 
    """
    subject = models.ForeignKey('TwitterAccount', related_name = 'subject', verbose_name=_('subject'))
    target = models.ForeignKey('TwitterAccount', related_name='target', verbose_name=_('target'))
    active = models.BooleanField(default=True) 
    created = models.DateTimeField(auto_now_add=True) # 
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        unique_together = (('subject', 'target'),)
        ordering = ('created',)
        verbose_name = _('Twitter Relationship')
        verbose_name_plural = _('Twitter Relationships')
        db_table = 'social_twitter_account_relationship'
    
class TwitterAccount(models.Model):
    """
    We will lazy load this thing.
    For the most part we will just leave the data to live in the account Relationships. 
    then when we take input from the UI that calls more data to show up on a particular 
    id that we will use that to populate this.  
    """
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    screen_name = models.CharField(max_length=25)
    location = models.CharField(max_length=100, null=True)
    profile_location = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=160, null=True)
    protected = models.BooleanField(default=False)
    followers_count = models.IntegerField(default=0)
    friends_count = models.IntegerField(default=0)
    listed_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    favourites_count = models.IntegerField(default=0)
    utc_offset = models.IntegerField(default=0, null=True)
    time_zone = models.CharField(max_length=35, null=True)
    geo_enabled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    statuses_count = models.IntegerField(default=0)
    lang = models.CharField(max_length=5,null=True)
    profile_image_url_https = models.CharField(max_length=150,null=True)
    following = models.BooleanField(default=False)
    follow_request_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # rate limiting 
    followers_updated = models.DateTimeField(auto_now=True)
    friends_updated = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return u'%s_%s' % (self.screen_name, self.id)
    
    class META:
        verbose_name=_('Twitter Account')
        verbose_name_plural=_('Twitter Accounts')
        db_table='social_twitter_account'
    

class TwitterApiRequest(models.Model):
    """
    For keeping track of the twitter API requests 
    primarily used for throttling 
    """
    twitter_id = models.BigIntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    request_name = models.CharField(max_length=45,db_index=True,null=False)
    request_status = models.IntegerField()


class LimitStatus(models.Model):
    """
    For tracking rate limits
    This will be created as a notice for those times when we encounter the rate limit error 
    """
    account_id = models.BigIntegerField(unique=True) # the social account 
    created = models.DateTimeField(auto_now_add=True) 
    request_name = models.CharField(max_length=15)
    active = models.BooleanField(default=True) # set to false after resolved... i can use this later
    
    
