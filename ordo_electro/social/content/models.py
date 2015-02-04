from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# simple quote 
class Quote(models.Model):
    quote_text_small = models.CharField(max_length=140)
    quote_text_orig = models.TextField()
    active = models.BooleanField(default=True)
    score = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.quote_text_small[:55]
    
    
class GRAuthor(models.Model):
    gr_author_id = models.IntegerField()
    name = models.CharField(max_length=55)
    image_url = models.CharField(max_length=255)
    small_image_url = models.CharField(max_length=255)
    author_page = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    