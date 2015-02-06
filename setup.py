#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#----------------------------------------------------------------------------
"""IETF RFC media type objects."""

from .__meta__ import (__version__, __author__, __copyright__, __license__)

import sys
if sys.version_info < (3, 2):
    raise Exception("pyietfrfc requires Python 3.2 or higher.")

import os

import locale
locale.setlocale(locale.LC_ALL, '')

from distutils.core import setup
from distutils.command.build import build

sys.path.insert(0, os.path.abspath("setup/lib"))
from distutils_local import *
build.sub_commands.append(('build_docutils', build_docutils.has_docs))


#Do the distutils setup
setup(
    name='ietfrfc',
    version=__version__,
    author='Lance Finn Helsten',
    author_email='lanhel@flyingtitans.com',
	#maintainer='',
    #maintainer_email='',
    url='http://www.flyingtitans.com/products/rest2py',
    description='IETF RFC media type representations.',
    long_description=open('README.rst', encoding='ascii').read(),
    license="Apache License, Version 2.0",    
    #scripts=[],
    #data_files=[],
    packages=['pyietflib',
        'pyietflib/iso8601',
        'pyietflib/rfc2045',
        'pyietflib/rfc5646',
        'pyietflib/rfc5870',
        'pyietflib/rfc6350'
    ],
    #package_dir={'' : 'src'},
    package_data = {
        'pyietflib/rfc5646': ['language-subtag-registry.txt']
    },
    requires=[
        "docutils (>0.8)"
    ],
    provides=[
    ],
    cmdclass={
        "test":test_unit,
        "accept":test_accept,
        "build_docutils":build_docutils
    }
)


