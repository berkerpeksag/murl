# coding: utf-8

from collections import namedtuple
from urlparse import urlparse, urlunparse

URL_PARAMS = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')
# See http://docs.python.org/library/urlparse.html#urlparse.ParseResult
ParseResult = namedtuple('ParseResult', ' '.join(URL_PARAMS))


class Url(object):
    def __init__(self, url, **kwargs):
        self._url = url
        self.params = dict((URL_PARAMS[k], v if v else None)
            for k, v in enumerate(urlparse(self._url)))

    @property
    def url(self):
        return urlunparse(ParseResult(**self.params))

    @property
    def scheme(self):
        return self.params.get('scheme')

    @scheme.setter
    def scheme(self, value):
        self.params['scheme'] = value

    @property
    def host(self):
        return self.params.get('netloc')

    @property
    def querystring(self):
        return self.params.get('query')

    def __str__(self):
        return self.url
