import os

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
