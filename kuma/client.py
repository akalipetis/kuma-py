"""
Defines the main Kuma Client app.
"""

import os

import requests

from .document import Document

class Client(object):
    def __init__(self, host='https://developer.mozilla.org', locale='en-US'):
        self.host = host
        self.locale = locale
        self.document = Document(self, '')

    @property
    def base_url(self):
        return os.path.join(self.host, self.locale)

    def __getattr__(self, name):
        return getattr(self.document, name)

    def get(self, endpoint, query=None, meta=None):
        url = os.path.join(self.base_url, endpoint)

        if (type(query) == list):
            query = '&'.join(query)

        if (query):
            url += '?%s' % query

        if (meta):
            url += '$%s' % meta

        response = requests.get(url)
        if (response.headers['content-type'].find('json') >= 0):
            response = response.json()
        else:
            response = response.text
        return response
