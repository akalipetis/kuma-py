import os

class Document(object):

    def __init__(self, client, endpoint):
        self.client = client
        self.endpoint = endpoint

    def get_child(self, name):
        return Document(self.client, os.path.join(self.endpoint, name))

    def __getattr__(self, name):
        return self.get_child(name)

    def __str__(self):
        return 'Kuma Document: %s' % self.url

    def get(self, query=None, meta=None):
        return self.client.get(self.endpoint, query=query, meta=meta)

    @property
    def raw(self):
        response = self.get(query='raw')
        return response

    @property
    def summary(self):
        return self.json()['summary']

    def section(self, section_id):
        pass
    
    def toc(self):
        response = self.get(meta='toc')
        return response

    def json(self):
        response = self.get(meta='json')
        return response

    def children(self):
        response = self.get(meta='children')
        return response

    def html(self):
        return self.get()
