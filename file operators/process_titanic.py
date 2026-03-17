from csv import DictReader

fr = open("file operators\titanic.csv")

# csv => list_of_diction [csv.py => DictReader]

data = list(DictReader(fr)) # print list of dictionary
print(data)


