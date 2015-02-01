# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from social_content import views

urlpatterns = patterns('',
    # URL pattern for the SCListView  # noqa
    url(
        regex=r'^$',
        view=views.SocialContentIndexView.as_view(),
        name='social_content'
    ),
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
    )
)
