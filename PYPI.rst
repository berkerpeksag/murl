murl
==========

.. image:: https://secure.travis-ci.org/berkerpeksag/murl.png
    :alt: Travis CI
    :target: http://travis-ci.org/berkerpeksag/murl

murl is a tiny wrapper for the Python module `urlparse <http://docs.python.org/library/urlparse.html>`_.

Installation
------------

To install murl, simply::

    $ pip install murl

Usage
-----

::

    from murl import Url


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

License
-------

All files that are part of this project are covered by the following license, except where explicitly noted.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.
