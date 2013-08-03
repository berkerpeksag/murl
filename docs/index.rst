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

    from murl import Url

    url = Url('https://bugzilla.mozilla.org/show_bug.cgi?id=698201#c0')


Mutating the :class:`Url` object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    url.scheme = 'http'
    url.host = 'bugzilla.webkit.org'


Objects
-------

.. class:: Url

   .. attribute:: url

   .. attribute:: scheme

   .. attribute:: host


.. _urlparse: http://docs.python.org/library/urlparse.html
.. _GitHub: https://github.com/berkerpeksag/murl/>
