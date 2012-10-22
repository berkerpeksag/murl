#!/usr/bin/env python
# coding: utf-8

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
    version=find_version('murl/__init__.py'),
    description='murl is a tiny wrapper for the Python module urlparse.',
    long_description=read('PYPI.rst'),
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    url='https://github.com/berkerpeksag/murl',
    packages=['murl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='Mozilla Public License, v. 2.0',
    classifiers=(
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
    ),
    test_suite='nose.collector',
)
