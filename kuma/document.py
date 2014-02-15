import os

class Document(object):

    def __init__(self, client, endpoint):
        self.client = client
        self.endpoint = endpoint

    def get_child(self, name):
        return Document(self.client, os.path.join(self.endpoint, name))

    def __getattr__(self, name):
        return self.get_child(name)

    def __unicode__(self):
        url = os.path.join(self.client.base_url, self.endpoint)
        return 'Kuma document at %s' % url

    def __str__(self):
        return self.__unicode__()

    def get(self, query=None, meta=None):
        return self.client.get(self.endpoint, query=query, meta=meta)

    @property
    def raw(self):
        response = self.get(query='raw')
        return response

    @property
    def summary(self):
        return self.json()['summary']

    def section(self, section_id, raw=True, macros=True):
        section = 'section=%s' % section_id
        query = [section]

        if (raw):
            query.append('raw')

        if (macros):
            query.append('macros')

        response = self.get(query=query)
        return response
    
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

    @property
    def subpages(self):
        # TODO: Lazify this
        subpage_list = self.children()['subpages']
        pages = []
        for subpage in subpage_list:
            pages.append(self.get_child(subpage['title']))
        return pages
