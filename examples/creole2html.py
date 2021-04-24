#!/usr/bin/python

import sys

from ..creole.parser import Parser
from ..creole.html_emitter import HtmlEmitter

if __name__ == "__main__":
    document = Parser(str(sys.stdin.read(), 'utf-8', 'ignore')).parse()
    sys.stdout.write(HtmlEmitter(document).emit().encode('utf-8', 'ignore'))

