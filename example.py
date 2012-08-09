#!/usr/bin/env python
# coding: utf-8

from urlparse2 import Url


def main():
    url = Url('https://bugzilla.mozilla.org/show_bug.cgi?id=698201#c0')
    print url.scheme, url.host, url.querystring, url.fragment
    # https bugzilla.mozilla.org id=698201 c0

    url.scheme = 'http'
    url.host = 'bugzilla.webkit.org'

    print url
    print url.url
    print url.scheme
    print url.host
    print url.netloc
    print url.host == url.netloc
    # http://bugzilla.webkit.org/show_bug.cgi?id=698201#c0
    # http://bugzilla.webkit.org/show_bug.cgi?id=698201#c0
    # http
    # bugzilla.webkit.org
    # bugzilla.webkit.org
    # True

    url.path = 'list_bugs.cgi'
    print url.path, url.url
    # list_bugs.cgi http://bugzilla.webkit.org/list_bugs.cgi?id=698201#c0

    url.fragment = 'c1'
    print url.fragment
    print url.url
    # c1
    # http://bugzilla.webkit.org/list_bugs.cgi?id=698201#c1

    url.fragment = ''
    print url.fragment
    print url.url
    # ''
    # http://bugzilla.webkit.org/list_bugs.cgi?id=698201

if __name__ == '__main__':
    main()
