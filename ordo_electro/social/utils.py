import httplib
import urlparse

'''
Created on Feb 23, 2015

@author: moz
'''

class Utils():

    @staticmethod
    def unshorten_url(url):
        parsed = urlparse.urlparse(url)
        h = httplib.HTTPConnection(parsed.netloc)
        h.request('HEAD', parsed.path)
        response = h.getresponse()
        if response.status/100 == 3 and response.getheader('Location'):
            return response.getheader('Location')
        else:
            return url