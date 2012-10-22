import sys

PY3 = sys.version_info[0] == 3

if PY3:
    unicode = str
else:
    unicode = unicode


def py2_unicode(klass):
    if not PY3:
        klass.__unicode__ = klass.__str__
        klass.__str__ = lambda self: self.__unicode__().encode('utf-8')
    return klass
