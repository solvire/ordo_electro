# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from social.content import views
from social.views import SocialAccountViewSet, SocialAccountTypeViewSet, TwitterAccountOverviewView, TwitterAccountViewSet, TwitterAccountRelationshipViewSet, oauth_redirect, oauth_verify, TwitterAccountFollowerViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_extensions.routers import ExtendedSimpleRouter

# router = routers.DefaultRouter()
# router.register(r'accounts', SocialAccountViewSet)

router = ExtendedSimpleRouter()
"""
TODO these need to be moved into a sub directory 
"""
(
    router.register(r'twitter/accounts',TwitterAccountViewSet,base_name='social-twitter-accounts',)
          .register(r'relationships',
                    TwitterAccountRelationshipViewSet,
                    base_name='social-twitter-account-relationships',
                    parents_query_lookups=['relationship__subject', 'account'])
)
(
    router.register(r'twitter/accounts',TwitterAccountViewSet,base_name='social-twitter-accounts',)
          .register(r'followers',
                    TwitterAccountFollowerViewSet,
                    base_name='social-twitter-account-followers',
                    parents_query_lookups=['relationship__subject', 'account'])
)
(
    router.register(r'accounts', SocialAccountViewSet,base_name='social-account',)
          .register(r'account_types',
                    SocialAccountTypeViewSet,
                    base_name='social-accounts-type',
                    parents_query_lookups=['account_types'])
                    
)


urlpatterns = patterns('',
    # URL pattern for the SCListView  # noqa
    url(
        regex=r'^quote_scheduler', 
        view=views.SocialContentQuoteScedulerView.as_view(), 
        name='quote_scheduler'
    ),
    url(
        regex=r'^quotes', 
        view=views.SocialContentQuotesView.as_view(), 
        name='quotes'
    ),
    url(
        regex=r'^tweets', 
        view=views.TweetsView.as_view()
    ),
 
    # An example view using a Twython method with proper OAuth credentials. Clone
    # this view and url definition to get the rest of your desired pages/functionality.
    url(
        regex=r'^twitter_timeline', 
        view=views.TwitterTimeline.as_view(), 
        name="twitter_timeline"
    ),
    url(
        regex=r'^content_dashboard', 
        view=views.ContentDashbaord.as_view(), 
        name="content_dashboard"
    ),
    url(r'^twitter_oauth_redirect/(?P<social_account_id>\d+)',oauth_redirect),
    url(r'^twitter_oauth_verify',oauth_verify),
    url(r'', include(router.urls)),
) 

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
