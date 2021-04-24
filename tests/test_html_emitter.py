#!/usr/bin/python

import os
import sys
import doctest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ..creole import html_emitter

if __name__ == "__main__":
    doctest.testmod(html_emitter)
