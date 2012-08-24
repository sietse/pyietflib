#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""`RFC 5646 <http://tools.ietf.org/html/rfc5646>`_ Tags for Identifying
Languages parser.
"""
__version__ = '1.0'
__copyright__ = """Copyright 2011 Lance Finn Helsten (helsten@acm.org)"""
__license__ = """
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
if sys.version_info < (3, 2):
    raise Exception("pyietflib requires Python 3.2 or higher.")


from .languagetag import *
from .registry import *


