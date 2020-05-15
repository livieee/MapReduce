import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split('::')
    name = line[1]
    genre_list = line[2]
    if genre_list != "":
        genre_list = genre_list.split('|')
    for genre in genre_list:
        print('%s\t%s' % (genre, name))
