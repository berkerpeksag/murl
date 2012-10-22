#!/usr/bin/env python
# coding: utf-8

import unittest

from murl import Url
from murl.utils import unicode


class TestMurl(unittest.TestCase):

    def test_parse_url(self):
        url = Url('http://www.mozilla.org/en-US/')
        self.assertEqual('http://www.mozilla.org/en-US/', str(url))
        self.assertEqual('http://www.mozilla.org/en-US/', url.url)
        self.assertEqual('http', url.scheme)
        self.assertEqual('www.mozilla.org', url.host)
        self.assertEqual('', url.querystring)

    def test_update_scheme(self):
        url = Url('http://githubbadge.appspot.com/badge/berkerpeksag?s=1')
        old_scheme = url.scheme
        self.assertEqual('http', url.scheme)
        url.scheme = 'https'
        self.assertEqual('https', url.scheme)
        self.assertNotEqual(old_scheme, url.scheme)

    def test_update_scheme_and_url(self):
        url_string = 'http://githubbadge.appspot.com/badge/berkerpeksag?s=1'
        url = Url(url_string)
        self.assertEqual(url_string, url.url)
        url.scheme = 'https'
        self.assertEqual(
            'https://githubbadge.appspot.com/badge/berkerpeksag?s=1', url.url)

    def test_update_host_and_url(self):
        url_string = 'http://githubbadge.appspot.com/badge/berkerpeksag?s=1'
        url = Url(url_string)
        old_host = url.host
        self.assertEqual('githubbadge.appspot.com', url.host)
        url.host = 'githubbadge.com'
        self.assertNotEqual(old_host, url.host)
        self.assertEqual(
            'http://githubbadge.com/badge/berkerpeksag?s=1', url.url)

    def test_update_path_and_url(self):
        url_string = 'http://githubbadge.appspot.com/badge/berkerpeksag?s=1'
        url = Url(url_string)
        old_path = url.path
        self.assertEqual('/badge/berkerpeksag', url.path)
        self.assertTrue(url.path.startswith('/'))
        url.path = 'badge/BYK'
        self.assertEqual('badge/BYK', url.path)
        self.assertNotEqual(old_path, url.path)
        self.assertEqual(
            'http://githubbadge.appspot.com/badge/BYK?s=1', url.url)

    def test_update_querystring_and_url(self):
        url = Url('http://githubbadge.appspot.com/badge/berkerpeksag?s=1&a=0')
        self.assertEqual('a=0&s=1', url.querystring)

    def test_url_with_port(self):
        url_string = 'http://test.python.org:5432/foo/#top'
        url = Url(url_string)
        self.assertEqual('test.python.org:5432', url.host)
        self.assertEqual('/foo/', url.path)

    def test_url_with_fragment(self):
        url_string = 'http://test.python.org:5432/foo/#top'
        url = Url(url_string)
        self.assertEqual('top', url.fragment)

    def test_change_scheme(self):
        url_str = '//www.python.org'
        url = Url(url_str, scheme='http')
        self.assertEqual('http', url.scheme)
        self.assertEqual('http://www.python.org', url.url)

    def test_rfc1808(self):
        url = Url('www.python.org')
        self.assertEqual('//www.python.org', url.host)

    def test_change_host(self):
        url_str = 'http://docs.python.org/library/urlparse.html'
        url = Url(url_str, netloc='dev.python.org')
        self.assertEqual('http', url.scheme)
        self.assertEqual('dev.python.org', url.host)
        self.assertEqual('http://dev.python.org/library/urlparse.html',
            url.url)

    def test_alias_host_netloc(self):
        url_str = 'http://docs.python.org/library/urlparse.html'
        url = Url(url_str, netloc='dev.python.org')
        self.assertEqual('dev.python.org', url.host)
        self.assertEqual('dev.python.org', url.netloc)
        self.assertEqual(url.netloc, url.host)
        self.assertEqual('http://dev.python.org/library/urlparse.html',
            url.url)

    def test_manipulate_querystring(self):
        url_string = 'http://example.com/berkerpeksag?s=1&a=0&b=berker'
        url = Url(url_string)
        self.assertEqual('a=0&s=1&b=berker', url.querystring)
        self.assertEqual({'a': ['0'], 's': ['1'], 'b': ['berker']}, url.qs)
        self.assertEqual(['0'], url.qs.get('a'))

    def test_unicode(self):
        url_str = r'http://www.python.org\U+0024'
        url = Url(url_str)
        self.assertEqual(url_str, unicode(url))


if __name__ == '__main__':
    unittest.main()
