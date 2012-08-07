# coding: utf-8

from urlparse import urlparse, urlunparse, ParseResult

URL_PARAMS = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')


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
