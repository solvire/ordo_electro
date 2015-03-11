from mongoengine import *
import datetime

class TwitterStatus(DynamicDocument):
    twitter_id = LongField()
    status_id = LongField(unique=True)
    created = DateTimeField(required=True)
    modified = DateTimeField(required=True, default=datetime.datetime.utcnow)
    
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(TwitterStatus, self).save(*args, **kwargs)

