import requests

class Document(object):

    def __init__(self, client, endpoint):
        self.client = client
        self.endpoint = endpoint

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
