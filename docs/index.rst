murl: URL manipulation in Python, made simple
=============================================

murl is a tiny wrapper for the Python module urlparse_.

:Source: https://github.com/berkerpeksag/murl/
:Issues: https://github.com/berkerpeksag/murl/issues/
:PyPI: http://pypi.python.org/pypi/murl/


Getting Started
---------------

Install with **pip**:

.. code-block:: bash

    $ pip install pyresto

or clone the latest version from GitHub_.


Usage
-----

Creating a :class:`Url` object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    >>> from murl import Url
    >>> url = Url('https://bugzilla.mozilla.org/show_bug.cgi?id=698201#c0')
    >>> url
    <Url: https://bugzilla.mozilla.org/show_bug.cgi?id=698201#c0>


Mutating the :class:`Url` object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    >>> url.scheme
    'https'
    >>> url.scheme = 'http'
    >>> url.scheme
    'http'


List all attributes of a :class:`Url` object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    >>> dir(url)
    [u'fragment', u'host', u'netloc', u'path', u'qs', u'querystring', u'scheme', u'url']


Objects
-------

.. class:: Url

   .. attribute:: url

   .. attribute:: scheme

   .. attribute:: host

   .. attribute:: path

   .. attribute:: querystring

   .. attribute:: qs

      Return a :class:`dict` of the current :attr:`querystring`
      attribute. For example::

          >>> url = Url('http://example.com/berkerpeksag?s=1&a=0&b=berker')
          >>> url.qs
          {'a': ['0'], 's': ['1'], 'b': ['berker']}

   .. attribute:: fragment


Hacking
-------

.. highlight:: bash

To setup a local development environment for hacking:

1. Clone the repo::

    $ git clone git://github.com/berkerpeksag/murl.git
    $ cd murl

2. Create and activate a new virtual environment::

    $ virtualenv <your_venv_name>
    $ source <your_venv_name>/bin/activate

3. Install required dependencies::

    $ pip install -r requirements-dev.txt

4. To run the tests, do::

    $ nosetests -v


.. _urlparse: http://docs.python.org/library/urlparse.html
.. _GitHub: https://github.com/berkerpeksag/murl/>
