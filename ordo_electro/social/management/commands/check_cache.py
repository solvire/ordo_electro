'''
Created on Mar 5, 2015

@author: moz
'''
from django.core.management.base import BaseCommand
from optparse import make_option
from django.core.cache import cache


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
        
        cache.set("key", "testing")
        cache.set("key", "testing2")
        cache.set('limit', cache.get('limit') + 2)
        print(cache.get('key'))
        print(cache.get('limit'))
    