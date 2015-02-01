# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import View, ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from social_content.models import Quote

class SocialContentIndexView(LoginRequiredMixin,View):
    template_name = 'social_content/index.html'
    
class SocialContentQuotesView(LoginRequiredMixin,ListView):
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
