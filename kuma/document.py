import os

import requests

class Document(object):

    def __init__(self, client, endpoint):
        self.client = client
        self.endpoint = endpoint

    def __getattr__(self, name):
        return Document(self.client, os.path.join(self.endpoint, name))

    def __str__(self):
        return 'Kuma Document: %s' % self.url

    @property
    def url(self):
        return os.path.join(self.client.base_url, self.endpoint)

    @property
    def raw(self):
        pass

    @property
    def macros(self):
        pass

    @property
    def nomacros(self):
        pass

    @property
    def summary(self):
        pass

    def section(self, section_id):
        pass

    def toc(self):
        pass

    def json(self):
        pass

    def children(self):
        pass
