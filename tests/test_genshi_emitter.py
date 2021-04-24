#!/usr/bin/python

import doctest

from ..creole import genshi_emitter

if __name__ == "__main__":
    doctest.testmod(genshi_emitter)
