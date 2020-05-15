#!/usr/bin/env python
"""reducer.py"""

import sys
from turtledemo.penrose import f

d = {};
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    city, count = line.split('\t', 1)
    # convert count (currently a string) to int
    if city in d:
        d[city] +=1
    else:
        d[city] = 1

with open('cityInformation','w') as f:
    for city in d:
        f.write('%s\t%s\n' % (city, d[city]))