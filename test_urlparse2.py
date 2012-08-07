#!/usr/bin/env python
# coding: utf-8

import unittest

from urlparse2 import Url


class TestUrlparse(unittest.TestCase):

    def test_parse_url(self):
        url = Url('http://www.mozilla.org/en-US/')
        self.assertEqual('http://www.mozilla.org/en-US/', url)
        self.assertEqual('http://www.mozilla.org/en-US/', url.url)
        self.assertEqual('http', url.scheme)
        self.assertEqual('www.mozilla.org', url.host)
        self.assertEqual(None, url.querystring)

if __name__ == '__main__':
    unittest.main()
