from django.db import models

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
    