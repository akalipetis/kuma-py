import os

from . import Document

class Client(object):
    def __init__(self, host='https://developer.mozilla.org', locale='en-US'):
        self.host = host
        self.locale = locale

    @property
    def base_url(self):
        return os.path.join(self.host, self.locale)
