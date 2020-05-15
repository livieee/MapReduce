#!/usr/bin/env python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter=',')
next(reader)
for row in reader:
         # Write the key-value pair to stdout to be processed by
         # the reducer.
         # The key is anything before the first tab character and the
         # value is anything after the first tab character.
    city = row[9]
    print('%s\t%s' % (city, 1))




