import os

class Document(object):
    """
    This is the kuma.Document class that defines a kuma Document. It lets you
    access it raw HTML data, summary, children pages etc. Basically it wraps
    the Kuma API in an easy, useful and elegand Python wrapper.
    """

    def __init__(self, client, endpoint):
        """
        Initializes a kuma.Document
        """
        self.client = client
        """Specify the kuma.Client to which requests will be delegated"""

        self.endpoint = endpoint
        """Specify the endpoint of the current document"""

    def get_child(self, name):
        """
        Return a child endpoint of the current document.
        """
        return Document(self.client, os.path.join(self.endpoint, name))

    def __getattr__(self, name):
        """
        This getter is used to provide attribute chaining, so as to get pretty
        Python code, while accessing _deep_ children in the current host.
        """
        return self.get_child(name)

    def __unicode__(self):
        url = os.path.join(self.client.base_url, self.endpoint)
        return 'Kuma document at %s' % url

    def __str__(self):
        return self.__unicode__()

    def get(self, query=None, meta=None):
        """
        Make a request to the client and return the result.
        """
        return self.client.get(self.endpoint, query=query, meta=meta)

    @property
    def raw(self):
        """
        Return raw html data for the current document.
        """
        response = self.get(query='raw')
        return response

    @property
    def summary(self):
        """
        Return the summary of the current document.
        """
        return self.json()['summary']

    def section(self, section_id, raw=True, macros=True):
        """
        Return a specific section of the current page in raw format with
        macros applied (meaning render the kuma templates)
        """
        section = 'section=%s' % section_id
        query = [section]

        if (raw):
            query.append('raw')

        if (macros):
            query.append('macros')

        response = self.get(query=query)
        return response
    
    def toc(self):
        """
        Returns the current document's Table of Contents in Python dict format.
        """
        response = self.get(meta='toc')
        return response

    def json(self):
        """
        Returns the current document's JSON data in Python dict format.
        """
        response = self.get(meta='json')
        return response

    def children(self):
        """
        Returns the children documents of this kuma Document in Python dict
        format.
        """
        response = self.get(meta='children')
        return response

    def html(self):
        """
        Returns the HTML code of the current kuma Document.
        """
        return self.get()

    @property
    def subpages(self):
        """
        Returns all the subpages of the current document in kuma.Document
        format.
        """
        # TODO: Lazify this
        subpage_list = self.children()['subpages']
        pages = []
        for subpage in subpage_list:
            pages.append(self.get_child(subpage['title']))
        return pages
