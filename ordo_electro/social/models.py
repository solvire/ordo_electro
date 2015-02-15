from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdown.extensions.headerid import unique

class Account(models.Model):
    owner_id = models.IntegerField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32, default='')
    account_id = models.BigIntegerField(default=0)
    account_type = models.ForeignKey('AccountType')
    active = models.BooleanField(default=True)
    token = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
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
    twitter_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=20)
    screen_name = models.CharField(max_length=25)
    location = models.CharField(max_length=25, null=True)
    profile_location = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=160, null=True)
    protected = models.BooleanField(default=False)
    followers_count = models.IntegerField(default=0)
    friends_count = models.IntegerField(default=0)
    listed_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    favourites_count = models.IntegerField(default=0)
    utc_offset = models.IntegerField(default=0, null=True)
    time_zone = models.CharField(max_length=15, null=True)
    geo_enabled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    statuses_count = models.IntegerField(default=0)
    lang = models.CharField(max_length=5,null=True)
    profile_image_url_https = models.CharField(max_length=150,null=True)
    following = models.BooleanField(default=False)
    follow_request_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
