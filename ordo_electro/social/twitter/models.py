from mongoengine import *

class TwitterStatus(DynamicDocument):
    twitter_id = LongField()
    status_id = LongField(unique=True)
    