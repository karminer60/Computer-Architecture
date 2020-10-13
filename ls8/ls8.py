#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load()
cpu.run()

if len(sys.argv) == 2:  # CPU file + file to be ran
    cpu = CPU()
    cpu.load(sys.argv[1])
    cpu.run()
else:
    print('Error: Please provide filename to execute instructions')
    sys.exit(1)
