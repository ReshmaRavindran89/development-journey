# read grade
# A = excellent
# B= good
# c= average
# _: = invalid

grade = input("Enter grade: ")
match grade:
    case "A":
        print("EXCELLENT")
    case "B":
        print("GOOD")
    case "C":
        print("AVERAGE")
    case _:
        print("INVALID")
        