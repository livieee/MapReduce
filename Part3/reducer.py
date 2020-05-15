import sys
from turtledemo.penrose import f

d = {};
# input comes from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    genre, movie = line.split('\t', 1)
    # convert count (currently a string) to int
    if genre in d:
        d[genre].append(movie)
    else:
        d[genre] = []
        d[genre].append(movie)

with open('genre','w') as f:
    for genre in d:
        f.write('%s\t%s\n' % (genre, d[genre]))

