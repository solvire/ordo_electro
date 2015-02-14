from django.db import models
from django.utils.translation import ugettext_lazy as _

class Account(models.Model):
    owner_id = models.IntegerField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32, default='')
    account_type = models.ForeignKey('AccountType')
    active = models.BooleanField(default=True)
    token = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created',)
        
class AccountType(models.Model):
    name = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    
class TwitterAccountRelationship(models.Model):
    """
    A follower/follow/relation list basically 
    """
    subject = models.ForeignKey('TwitterAccount', related_name = 'subject', verbose_name=_('subject'))
    target = models.ForeignKey('TwitterAccount', related_name='target', verbose_name=_('target'))
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = (('subject', 'target'),)
        ordering = ('created',)
        verbose_name = _('Twitter Relationship')
        verbose_name_plural = _('Twitter Relationships')
    
class TwitterAccount(models.Model):
    """
    We will lazy load this thing.
    For the most part we will just leave the data to live in the account Relationships. 
    then when we take input from the UI that calls more data to show up on a particular 
    id that we will use that to populate this.  
    """
    twitter_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    screen_name = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    profile_location = models.CharField(max_length=45)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=160)
    protected = models.BooleanField(default=False)
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    listed_count = models.IntegerField()
    created_at = models.DateTimeField()
    favourites_count = models.IntegerField()
    utc_offset = models.IntegerField()
    time_zone = models.CharField(max_length=15)
    geo_enabled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    statuses_count = models.IntegerField()
    lang = models.CharField(max_length=5)
    profile_image_url_https = models.CharField(max_length=15)
    following = models.BooleanField(default=False)
    follow_request_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
