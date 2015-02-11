# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from social.content import views
from social.views import AccountViewSet, AccountTypeViewSet
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter

# router = routers.DefaultRouter()
# router.register(r'accounts', AccountViewSet)

router = ExtendedSimpleRouter()
(
    router.register(r'accounts', AccountViewSet,base_name='account',)
          .register(r'account_types',
                    AccountTypeViewSet,
                    base_name='accounts-type',
                    parents_query_lookups=['user_groups'])

)

urlpatterns = patterns('',
    # URL pattern for the SCListView  # noqa
#     url(
#         regex=r'^$',
#         view=views.SocialContentIndexView.as_view(),
#         name='social'
#     ),
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
    url(r'^', include(router.urls)),
) 
