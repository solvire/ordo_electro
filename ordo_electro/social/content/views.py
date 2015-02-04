# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings

from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import View, ListView, TemplateView
from twython import Twython


# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from social.content.models import Quote

class SocialContentIndexView(LoginRequiredMixin,View):
    template_name = 'social_content/index.html'
    
class SocialContentQuotesView(LoginRequiredMixin,ListView):
    template_name = "social_content/quote_list.html"
    permanent = False
    model = Quote
    # These next two lines tell the view to index lookups by username
    slug_field = "id"
    slug_url_kwarg = "id"
    
class SocialContentQuoteScedulerView(LoginRequiredMixin,View):
    template_name = 'social_content/quote_scheduler.html'
#     form_class = UploadForm

class TweetsView(View):
    template_name = "social_content/tweets.html"
    
class TwitterTimeline(TemplateView):
    """An example view with Twython/OAuth hooks/calls to fetch data about the user in question."""
    permanent = False
    template_name = 'social_content/twitter_timeline.html'
    
    def get_context_data(self, **kwargs):
        twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                          settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
        
        context = super(TwitterTimeline, self).get_context_data(**kwargs)
        context['tweets'] = twitter.get_favorites()
        return context
    
class ContentDashbaord(TemplateView):
    """Main Dashboard"""
    permanent = False
    template_name = 'social_content/content_dashboard.html'
    
    def get_context_data(self, **kwargs):
        twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET,
                          settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
        
        context = super(TwitterTimeline, self).get_context_data(**kwargs)
        context['tweets'] = twitter.get_favorites()
        return context
    
    
    
#     render_to_response('social_content/twitter_timeline.html', {'user_tweets': user_tweets})

