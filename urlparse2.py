#!/usr/bin/env python
# coding: utf-8

from urlparse import urlparse

URL_PARAMS = ['scheme', 'netloc', 'path', 'params', 'query', 'fragment']


class InvalidParameter(ValueError):
    pass


class Url(object):
    def __init__(self, url, **kwargs):
        self.url = url
        self.params = dict((URL_PARAMS[k], v if v else None)
            for k, v in enumerate(self._parse_url()))

    def _parse_url(self):
        return urlparse(self.url)

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
