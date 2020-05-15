from indexer import Indexer

if __name__ == '__main__':
    query = input("Enter the Genre: ")
    query = query.split(' ')
    model = Indexer(filename = "movies.dat")
    model.fit()
    if len(query) == 1:
        genre = query[0]
        names = model.get(genre)
        for name in names:
            print(name)
    else:
        genre1 = query[0]
        genre2 = query[2]
        if query[1].lower() == 'or':
            names = model.getOr(genre1, genre2)
            for name in names:
                print(name)
        elif query[1].lower() == 'and':
            names = model.getAnd(genre1, genre2)
            for name in names:
                print(name)