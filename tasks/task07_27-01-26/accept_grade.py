# 8. Create a program using match–case that accepts a grade (A, B, C, D, F) 
#  prints the result message.

grade = input("Enter grade : ")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")
              