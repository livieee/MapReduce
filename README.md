# Part 1: Determine the number of Starbucks in a City 
You have a dataset consisting of information about each Starbucks location.  You are to use MapReduce to provide for each city the number of Starbucks located in that city.  The input is a csv file, starbucks-locations.csv, and the output should be a  file, cityInformation, where each line represents a city and the number of Starbucks located  in that city. 


# Part 2: Inverted Index 
You are to build an inverted index that supports queries for movies based on movie genres.     A query can take one of the following forms:

- A single movie genre  e.g., Drama, Comedy.

- Boolean search queries with either only AND or only OR.  For example, “Drama OR Comedy” or “Drama AND Comedy”.   You only need to support the use of one Boolean operator and the user should be able to assume that your program is case agnostic.

Some of the movies are not associated with a genre.  You should have an entry, “ None”, for those movies.

# Part 3:    Inverted Index  
You are to build an inverted index using MapReduce with the same functionality as in Part 2.

 
The file with the map code should be mapper.py, the file with the reducer code should be reducer.py and the file with the query code should be query.py.

 

 

 
