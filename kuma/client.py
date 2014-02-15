"""
This module defines the kuma.Client class that handles the
interaction between kuma.Document and kuma web services.
"""

import os

import requests

from .document import Document


class Client(object):
    """
    This is the kuma.Client class that takes care of the communication with
    kuma servers. kuma.Client is locale-aware. kuma.Client.host defaults to
    the public Mozilla Developer Network URL and the default locale is
    United States English.
    """
    def __init__(self, host='https://developer.mozilla.org', locale='en-US'):
        """
        Initializes the kuma.Client by settings up the host, locale and
        document attributes.
        """
        self.host = host
        self.locale = locale
        self.document = Document(self, '')

    @property
    def base_url(self):
        """
        Returns the base URL of the current kuma.Client instance. Used to fetch
        documents.
        """
        return os.path.join(self.host, self.locale)

    def __getattr__(self, name):
        """
        This automatic getter is used to allow chaining of documents and
        provide pretty syntax like `kuma.Client().docs.web.api.location.json()`
        """
        return getattr(self.document, name)

    def get(self, endpoint, query=None, meta=None):
        """
        Returns a specific resource on the current kuma host. Can accept
        queries so as to return raw html, specific sections, children pages,
        return the page in JSON format etc.
        """
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
