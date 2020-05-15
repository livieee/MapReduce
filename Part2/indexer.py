import sys

class Indexer:
    
    def __init__(self, filename):
        self.filename = filename
        self.dict = {}
        self.dict["None"] = []
        
    def fit(self):
        file = open(self.filename, 'r')
        for row in file:
            row = row.split('::')
            id1 = row[0]
            name = row[1]
            genres = row[2]
            genres = genres[:-1]  # remove the new line character
            genres = genres.split('|')
            if genres[0] == "":
                self.dict["None"].append(name)
            for genre in genres:
                if not genre in self.dict:
                    self.dict[genre] = []
                self.dict[genre].append(name)
        
    def get(self, genre):
        return self.dict[genre]

    def getAnd(self, genre1, genre2):
        list1 = self.dict[genre1]
        set1 = set(list1)
        list2 = self.dict[genre2]
        set2 = set(list2)
        return set1.intersection(set2)

    def getOr(self, genre1, genre2):
        list1 = self.dict[genre1]
        set1 = set(list1)
        list2 = self.dict[genre2]
        set2 = set(list2)
        return set1.union(set2)
    
