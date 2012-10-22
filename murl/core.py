# coding: utf-8

try:
    from urllib.parse import (urlencode, urlparse, urlunparse,
                              parse_qs, ParseResult)
except ImportError:
    from urllib import urlencode
    from urlparse import urlparse, urlunparse, parse_qs, ParseResult

from murl.utils import py2_unicode

#: Parts for RFC 3986 URI syntax
#: <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
URL_PARTS = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')


@py2_unicode
class Url(object):
    """Parse (absolute and relative) URLs for humans."""

    def __init__(self, url, **parts):
        """
        Constructor for Url object.

        :param url:
        :type url: string

        :param parts: scheme, netloc, path, params,
                      query, fragment
        :type parts: dict
        """
        self._url = url
        self.params = dict((URL_PARTS[k], v)
            for k, v in enumerate(urlparse(self._url)))

        for option, value in parts.items():
            if option in parts:
                self.params[option] = value

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
        # Following the syntax specifications in RFC 1808,
        # urlparse recognizes a netloc only if it is properly
        # introduced by ‘//’. Otherwise the input is presumed
        # to be a relative URL and thus to start with a path component.
        if self.params.get('path').startswith('www.'):
            self.params['netloc'] = '//' + self.params.get('path')
            self.params['path'] = ''
        return self.params.get('netloc')

    @property
    def netloc(self):
        return self.host

    @host.setter
    def host(self, value):
        self.params['netloc'] = value

    @property
    def path(self):
        return self.params.get('path')

    @path.setter
    def path(self, value):
        self.params['path'] = value

    @property
    def querystring(self):
        if self.params.get('query'):
            return urlencode(parse_qs(self.params.get('query')), doseq=True)
        return ''

    @property
    def qs(self):
        return parse_qs(self.params.get('query'))

    @property
    def fragment(self):
        return self.params.get('fragment')

    @fragment.setter
    def fragment(self, value):
        self.params['fragment'] = value

    def __str__(self):
        return self.url
