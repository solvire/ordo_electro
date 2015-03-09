'''
Created on Mar 9, 2015

@author: moz
'''
from django.core.management.base import BaseCommand
from optparse import make_option
from social.twitter.models import TwitterStatus


class Command(BaseCommand):
    help = ('''Querying the cache for various keys - be careful you might drink from a firehose''')
    
    option_list = BaseCommand.option_list + (
        make_option(
            "-k", 
            "--cache_key", 
            dest = "cache_key",
            help = "Key to search the cache for", 
            metavar = "KEY"
        ),
    )
    
    
    
    def handle(self, *args, **options):
        """
        Print out the keys 
        """
        status = TwitterStatus.objects.get_or_create(status_id=123)
#         status.tags = ['mongodb', 'mongoengine']
        print(status[0].id)
    