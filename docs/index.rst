#############################################
murl: URL manipulation in Python, made simple
#############################################

murl is a tiny wrapper for the Python module urlparse_.

:Source: https://github.com/berkerpeksag/murl/
:Issues: https://github.com/berkerpeksag/murl/issues/
:PyPI: http://pypi.python.org/pypi/murl/
:Build status:
    .. image:: https://secure.travis-ci.org/berkerpeksag/murl.png
        :alt: Travis CI
        :target: http://travis-ci.org/berkerpeksag/murl/


Getting Started
===============

Install with **pip**:

.. code-block:: bash

    $ pip install murl

or clone the latest version from GitHub_.


Usage
=====

Creating a :class:`Url` object
------------------------------

::

    >>> from murl import Url
    >>> url = Url('https://bugzilla.mozilla.org/show_bug.cgi?id=698201#c0')
    >>> url
    <Url: https://bugzilla.mozilla.org/show_bug.cgi?id=698201#c0>


Mutating the :class:`Url` object
--------------------------------

::

    >>> url.scheme
    'https'
    >>> url.scheme = 'http'
    >>> url.scheme
    'http'

You can also change the *port* attribute if it is defined::

    >>> url = Url('http://test.python.org:8080/foo/#top')
    >>> url.port
    8080
    >>> url.port = 3000
    >>> url.port
    3000


List all attributes of a :class:`Url` object
--------------------------------------------

::

    >>> dir(url)
    [u'fragment', u'host', u'netloc', u'path', u'port', u'qs', u'querystring', u'scheme', u'url']


Objects
=======

.. class:: Url(url[, \*\*parts])

   The *url* parameter should be a :class:`str` object.

   The *parts* dictionary should be one of them: ``scheme``, ``netloc``,
   ``path``, ``params``, ``query``, ``fragment``.

   ::

       >>> url = murl.Url('http://www.google.com', path='about')
       >>> url
       <Url: http://www.google.com/about>


   .. attribute:: url

   .. attribute:: scheme

   .. attribute:: host

   .. attribute:: path

   .. attribute:: port

      .. versionadded:: 0.5

   .. attribute:: querystring

   .. attribute:: qs

      Return a :class:`dict` of the current :attr:`querystring`
      attribute. For example::

          >>> url = Url('http://example.com/berkerpeksag?s=1&a=0&b=berker')
          >>> url.qs
          {'a': ['0'], 's': ['1'], 'b': ['berker']}

   .. attribute:: fragment

   .. method:: __repr__

      .. versionadded:: 0.4


Changelog
=========

0.5.1
-----

:Release date: 2014-09-17

* Fix installation in Python 3.

0.5.0
-----

:Release date: 2013-12-02

* Add a *port* attribute to the :class:`Url`. (Contributed by Aaron Bassett)


Hacking
=======

.. highlight:: bash

To setup a local development environment for hacking:

1. Clone the repo::

    $ git clone https://github.com/berkerpeksag/murl.git
    $ cd murl

2. Create and activate a new virtual environment::

    $ python3.4 -m venv <your_venv_name>
    $ . <your_venv_name>/bin/activate

3. Install required dependencies::

    $ pip install -r requirements-dev.txt

4. To run the tests, do::

    $ nosetests


License
=======

All files that are part of this project are covered by the following
license, except where explicitly noted.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.


.. _urlparse: http://docs.python.org/library/urlparse.html
.. _GitHub: https://github.com/berkerpeksag/murl/
