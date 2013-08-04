import codecs
import os.path
import re

from distutils.core import setup


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path).read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='murl',
    version=find_version('murl.py'),
    description='murl is a tiny wrapper for the Python module urlparse.',
    long_description=read('PYPI.rst'),
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    url='https://github.com/berkerpeksag/murl',
    py_modules=['murl'],
    platforms='any',
    license='Mozilla Public License, v. 2.0',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ),
)
