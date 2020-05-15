filename = "genre"
file = open(filename)
d = {}
for row in file:
    genre, movie_list = row.split("\t")
    movie_list = movie_list.replace('"', "'")
    movie_list = movie_list[2: -3]
    movie_list = movie_list
    d[genre] = movie_list

#funtion of AND
def and_operator(x,y):
    for dict_genre in d:
        if x.lower() in dict_genre.lower():
            g1 = set(d[dict_genre].split("', '"))
        if y.lower() in dict_genre.lower():
            g2 = set(d[dict_genre].split("', '"))
    print (g1.intersection(g2))


def or_operator(x,y):
    for dict_genre in d:
        if x.lower() in dict_genre.lower():
            g1 = set(d[dict_genre].split("', '"))
        if y.lower() in dict_genre.lower():
            g2 = set(d[dict_genre].split("', '"))
    print (g1.union(g2))


def main():
    query = input("Enter the Genre: ")
    query = query.split(' ')
    match = False

    if len(query) == 1:
        for genre in d:
            if query[0].lower() in genre.lower():
                print (genre + " has movie: " + d[genre] )
                match = True
    else:
        if query[1].lower() == "and":
            and_operator(query[0], query[2])
            match = True
        elif query[1].lower == "or":
            or_operator(query[0], query[2])
            match = True

    if not match:
        print("No information of " )

if __name__ == '__main__':
    main()
