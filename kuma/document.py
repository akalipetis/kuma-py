import os

import requests

class Document(object):

    _dict_cache = None

    def __init__(self, client, endpoint):
        self.client = client
        self.endpoint = endpoint

    def get_child(self, name):
        return Document(self.client, os.path.join(self.endpoint, name))

    def __getattr__(self, name):
        return self.get_child(name)

    def __str__(self):
        return 'Kuma Document: %s' % self.url

    @property
    def url(self):
        return os.path.join(self.client.base_url, self.endpoint)

    @property
    def raw(self):
        pass

    @property
    def summary(self):
        return self.json()['summary']

    def section(self, section_id):
        pass
    
    def _get_meta(self, meta):
        url = '%s$%s' % (self.url, meta)
        return requests.get(url)

    def toc(self):
        response = self._get_meta('toc')
        return response.text

    def json(self, no_cache=False):
        if (not self._dict_cache or no_cache):
            response = self._get_meta('json')
            self._dict_cache = response.json()
        return self._dict_cache

    def children(self):
        response = self._get_meta('children')
        return response.json()

    def html(self):
        return requests.get(self.url).text
