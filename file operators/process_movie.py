from csv import DictReader

fr = open("file operators\\movie.csv")

data = list(DictReader(fr)) # print list of dictionary
print(data)

movie_wise_summary = {}



