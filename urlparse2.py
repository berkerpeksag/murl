# coding: utf-8

from urlparse import urlparse, urlunparse, parse_qs, ParseResult

#: Parts for RFC 3986 URI syntax
#: <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
URL_PARTS = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')


class Url(object):
    def __init__(self, url, **kwargs):
        self._url = url
        self.params = dict((URL_PARTS[k], v)
            for k, v in enumerate(urlparse(self._url)))
        for option, value in kwargs.items():
            if option in kwargs and not self.params.get(option):
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
        if self.params.get('query') is not None:
            return parse_qs(self.params.get('query'))
        return None

    @property
    def fragment(self):
        return self.params.get('fragment')

    def __str__(self):
        return self.url
