#!/usr/bin/env python
# coding: utf-8

import unittest

from urlparse2 import Url


class TestUrlparse(unittest.TestCase):

    def test_parse_url(self):
        url = Url('http://www.mozilla.org/en-US/')
        self.assertEqual('http://www.mozilla.org/en-US/', str(url))
        self.assertEqual('http://www.mozilla.org/en-US/', url.url)
        self.assertEqual('http', url.scheme)
        self.assertEqual('www.mozilla.org', url.host)
        self.assertEqual(None, url.querystring)

    def test_update_scheme(self):
        url = Url('http://githubbadge.appspot.com/badge/berkerpeksag?s=1')
        old_scheme = url.scheme
        self.assertEqual('http', url.scheme)
        url.scheme = 'https'
        self.assertEqual('https', url.scheme)
        self.assertNotEqual(old_scheme, url.scheme)

    def test_update_scheme_and_url(self):
        url = Url('http://githubbadge.appspot.com/badge/berkerpeksag?s=1')
        self.assertEqual('http://githubbadge.appspot.com/badge/berkerpeksag?s=1', str(url))
        url.scheme = 'https'
        self.assertEqual('https://githubbadge.appspot.com/badge/berkerpeksag?s=1', str(url))

if __name__ == '__main__':
    unittest.main()
