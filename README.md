# Urlparse2

```py
>>> from urlparse2 import Url
>>> url = Url('http://www.mozilla.org/en-US/')
>>> print url
http://www.mozilla.org/en-US/
>>> print url.scheme
http
>>> url.scheme = 'https'
>>> print url
https://www.mozilla.org/en-US/
```
